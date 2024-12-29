from dataclasses import dataclass
from collections import UserList
from random import randint, seed, choice
import time
import argparse

GLOBALS = {
    "MAP_BOUNDARIES": None,
}

@dataclass
class MapBoundaries:
    x: tuple
    y: tuple


class Location:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'[{self.x}; {self.y}]'

    def copy(self):
        return Location(**self.__dict__)

    def is_valid_location(self):
        if (GLOBALS["MAP_BOUNDARIES"].x[0] <= self.x <= GLOBALS["MAP_BOUNDARIES"].x[1]
            and GLOBALS["MAP_BOUNDARIES"].y[0] <= self.y <= GLOBALS["MAP_BOUNDARIES"].y[1]):
            return True
        else:
            return False


class Randomizer:

    def __init__(self, random_state):
        seed(random_state)

    def create_random_location(self):
        x = randint(GLOBALS["MAP_BOUNDARIES"].x[0], GLOBALS["MAP_BOUNDARIES"].x[1])
        y = randint(GLOBALS["MAP_BOUNDARIES"].y[0], GLOBALS["MAP_BOUNDARIES"].y[1])
        return Location(x, y)


class Player:
    """General game agent abstraction."""
    def __init__(self, name: str, location: Location):
        self._name = name
        self._location = location
        self._moves = None

    def __repr__(self):
        return f'Player {self._name} at [{self._location.x}, {self._location.y}]'

    @staticmethod
    def _move_left(new_potential_location):
        new_potential_location.x -= 1
        return new_potential_location

    @staticmethod
    def _move_right(new_potential_location):
        new_potential_location.x += 1
        return new_potential_location

    @staticmethod
    def _move_down(new_potential_location):
        new_potential_location.y -= 1
        return new_potential_location

    @staticmethod
    def _move_up(new_potential_location):
        new_potential_location.y += 1
        return new_potential_location

    @staticmethod
    def _move_pass(new_potential_location):
        return new_potential_location

    def move(self, where: str):
        assert where in {'left', 'right', 'up', 'down', 'pass'}
        moves = {
            'left': self._move_left, 
            'right': self._move_right,
            'up': self._move_up,
            'down': self._move_down,
            'pass': self._move_pass
        }
        move_func = moves[where]
        new_potential_location = self._location.copy()
        new_potential_location = move_func(new_potential_location)
        if new_potential_location.is_valid_location:
            self._location = new_potential_location

    def random_move(self):
        self.move(choice(self._moves))


class Hunter(Player):

    def __init__(self, location: Location):
        super().__init__(name="Hunter", location=location)
        self._moves = ['left', 'right', 'up', 'down']

    def  __repr__(self):
        return f'Hunter at [{self._location.x}, {self._location.y}]'

class Prey(Player):

    def __init__(self, name: str, location: Location):
        super().__init__(name, location)
        self._moves = ['left', 'right', 'up', 'down'] + 3*['pass']


class PreyList(UserList):

    def random_move(self):
        for player in self:
            player.random_move()

class Game:
    """High level game management."""
    def __init__(self, randomizer):
        self._players = PreyList()
        self._hunter = None
        self._randomizer = randomizer

    def add_player(self, player_name):
        new_player = Prey(
            name = player_name,
            location = self._randomizer.create_random_location()
        )
        self._players.append(new_player)

    def add_hunter(self):
        self._hunter = Hunter(
            location = self._randomizer.create_random_location()
        )

    def show_grid(self):
        for player in self._players:
            print(player)
        print(self._hunter)

    def make_move(self):
        print('----------------------------')
        self._hunter.random_move()
        self._players.random_move()
    
    def perform_killings(self):
        """Kill prey if possible."""
        print("Killing")


def set_game(args: argparse.Namespace) -> Game:
    GLOBALS["MAP_BOUNDARIES"] = MapBoundaries(
        x = (0, args.grid_size_x - 1),
        y = (0, args.grid_size_y - 1)
    )

    randomizer = Randomizer(random_state = 1)
    game = Game(randomizer)
    for prey_id in range(args.n_prey):
        game.add_player(player_name = f'Prey_{prey_id}')
    game.add_hunter()

    return game

def main(args: argparse.Namespace):
    print(f"Simulation parameters: {vars(args)}")
    game = set_game(args)

    # game loop
    for _ in range(args.n_steps):
        time.sleep(0.5)
        game.make_move()
        game.perform_killings()
        game.show_grid()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Hunter-killer',
        description='Simulation of one hunter and one or multiple prey',
    )
    parser.add_argument(
        '--n_prey', 
        default=2,
        type=int,
        help = 'Number of prey'
    )
    parser.add_argument(
        '--n_steps', 
        default=20,
        type=int,
        help = 'Number of simulation steps'
    )
    parser.add_argument(
        '--grid_size_x', 
        default=30,
        type=int,
        help = 'Grid size in X dimention'
    )
    parser.add_argument(
        '--grid_size_y', 
        default=30,
        type=int,
        help = 'Grid size in Y dimention'
    )
    args = parser.parse_args()
    main(args)
