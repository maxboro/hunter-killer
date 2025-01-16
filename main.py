from collections import UserList
from random import randint, seed, choice
import time
import copy
from typing import Self

class Settings:
    """Settings singletone abstraction"""
    def __new__(cls) -> Self:
        if not hasattr(cls, "instance"):
            cls.instance = super(Settings, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self._settings = {}
            self._initialized = True
            self._load()

    def __repr__(self) -> str:
        return str(self._settings)

    def _calc_derivative_parameters(self) -> None:
        self._settings["map_boundaries"] = {
            "x": {"min": 0, "max": self._settings["grid_size_x"] - 1},
            "y": {"min": 0, "max": self._settings["grid_size_y"] - 1},
        }

    def _load(self) -> None:
        with open("settings.txt", "r") as settings_file:
            settings_str = settings_file.read()

        settings_lines = settings_str.split("\n")
        for line in settings_lines:
            if "=" in line:
                name, value = line.split("=")
                self._settings[name] = int(value)
        self._calc_derivative_parameters()

    def get(self, setting_name: str):
        if setting_name in self._settings:
            return self._settings[setting_name]
        else:
            raise ValueError(f"{setting_name} is not in settings")

class Location:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self._map_boundaries = Settings().get("map_boundaries")

    def __repr__(self) -> str:
        return f'[{self.x}; {self.y}]'

    def __eq__(self, other) -> bool:
        return isinstance(other, Location) and self.x == other.x and self.y == other.y

    def copy(self) -> Self:
        return Location(self.x, self.y)

    def is_valid_location(self) -> bool:
        validity = (
            self._map_boundaries["x"]["min"] <= self.x <= self._map_boundaries["x"]["max"]
            and self._map_boundaries["y"]["min"] <= self.y <= self._map_boundaries["y"]["max"]
        )
        return validity


class Randomizer:
    """Pseudorandom number utils."""
    def __init__(self, random_state: int) -> None:
        seed(random_state)
        self._map_boundaries = Settings().get("map_boundaries")

    def create_random_location(self) -> Location:
        x = randint(self._map_boundaries["x"]["min"], self._map_boundaries["x"]["max"])
        y = randint(self._map_boundaries["y"]["min"], self._map_boundaries["x"]["max"])
        return Location(x, y)


class Player:
    """General game agent abstraction."""
    def __init__(self, name: str, location: Location) -> None:
        self._name = name
        self._location = location
        self._moves = None
        self._is_alive = True
        self.sign = None

    def __repr__(self) -> str:
        return f'Player {self._name} at [{self._location.x}, {self._location.y}]'

    @staticmethod
    def _move_left(new_potential_location) -> Location:
        new_potential_location.x -= 1
        return new_potential_location

    @staticmethod
    def _move_right(new_potential_location) -> Location:
        new_potential_location.x += 1
        return new_potential_location

    @staticmethod
    def _move_down(new_potential_location) -> Location:
        new_potential_location.y -= 1
        return new_potential_location

    @staticmethod
    def _move_up(new_potential_location) -> Location:
        new_potential_location.y += 1
        return new_potential_location

    @staticmethod
    def _move_pass(new_potential_location) -> Location:
        return new_potential_location

    def move(self, where: str) -> None:
        assert where in {'left', 'right', 'up', 'down', 'pass'}
        moves = {
            'left': self._move_left, 
            'right': self._move_right,
            'up': self._move_up,
            'down': self._move_down,
            'pass': self._move_pass
        }
        if self._is_alive:
            move_func = moves[where]
        else:
            move_func = moves['pass']
        new_potential_location = self._location.copy()
        new_potential_location = move_func(new_potential_location)
        if new_potential_location.is_valid_location():
            self._location = new_potential_location

    def random_move(self) -> None:
        self.move(choice(self._moves))

    def get_location(self) -> Location:
        return self._location

    def get_name(self) -> str:
        return self._name


class Hunter(Player):

    def __init__(self, location: Location) -> None:
        super().__init__(name="Hunter", location=location)
        self._moves = ['left', 'right', 'up', 'down']
        self.sign = "H"

    def  __repr__(self) -> str:
        return f'Hunter at [{self._location.x}, {self._location.y}]'

class Prey(Player):

    def __init__(self, name: str, location: Location) -> None:
        super().__init__(name, location)
        self._moves = ['left', 'right', 'up', 'down'] + 3*['pass']
        self.sign = "P"

    def  __repr__(self) -> str:
        alive_info = "Is alive." if self._is_alive else "Is dead"
        return f'{self._name} at [{self._location.x}, {self._location.y}]. {alive_info}'

    def kill(self) -> None:
        self._is_alive = False
        self.sign = "X"


class PreyList(UserList):

    def random_move(self) -> None:
        for prey in self:
            prey.random_move()

class Game:
    """High level game management."""
    def __init__(self, randomizer: Randomizer, show_grid: int) -> None:
        self._prey = PreyList()
        self._hunter = None
        self._randomizer = randomizer
        self._to_show_grid = bool(show_grid)
        self._map_boundaries = Settings().get("map_boundaries")
        self._empty_grid = [[
            ' ' for el in range(self._map_boundaries["x"]["max"] + 1)] 
            for line in range(self._map_boundaries["y"]["max"] + 1)
        ]
        self._populated_grid = None

    def add_prey(self, prey_name: str) -> None:
        new_prey = Prey(
            name = prey_name,
            location = self._randomizer.create_random_location()
        )
        self._prey.append(new_prey)

    def add_hunter(self) -> None:
        self._hunter = Hunter(
            location = self._randomizer.create_random_location()
        )

    def _show_grid(self) -> None:
        populated_grid = copy.deepcopy(self._empty_grid)

        # add prey
        for prey in self._prey:
            loc = prey.get_location()
            populated_grid[loc.y][loc.x] = prey.sign

        # add hunter
        loc = self._hunter.get_location()
        populated_grid[loc.y][loc.x] = self._hunter.sign

        # save current grid
        self._populated_grid = populated_grid

        # print grid
        grid_print = '\n'.join(["|".join(line) for line in self._populated_grid])
        print(grid_print)

    def show_status(self) -> None:
        for prey in self._prey:
            print(prey)
        print(self._hunter)
        if self._to_show_grid:
            self._show_grid()

    def make_move(self) -> None:
        print('----------------------------')
        self._hunter.random_move()
        self._prey.random_move()

    def perform_killings(self) -> None:
        """Kill prey if possible."""
        hunter_current_location = self._hunter.get_location()
        for prey in self._prey:
            if prey.get_location() == hunter_current_location:
                prey.kill()
                print(f"{prey.get_name()} is killed.")


def set_game(settings: Settings) -> Game:
    randomizer = Randomizer(random_state = 1)
    game = Game(randomizer, settings.get("show_grid"))
    for prey_id in range(settings.get("n_prey")):
        game.add_prey(prey_name = f'Prey_{prey_id}')
    game.add_hunter()

    return game

def main():
    settings = Settings()

    print(f"Simulation parameters: {settings}")
    game = set_game(settings)

    # start locations
    game.show_status()

    # game loop
    for _ in range(settings.get("n_steps")):
        time.sleep(0.5)
        game.make_move()
        game.perform_killings()
        game.show_status()

if __name__ == '__main__':
    main()
