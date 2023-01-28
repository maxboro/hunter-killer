from dataclasses import dataclass
from collections import UserList
from random import randint, seed, choice
import time

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
    
    def is_valid_location(self, new_potential_location):
        if (MAP_BOUNDARIES.x[0] <= self.x <= MAP_BOUNDARIES.x[1] 
            and MAP_BOUNDARIES.y[0] <= self.y <= MAP_BOUNDARIES.y[1]):
            return True
        else:
            return False
        
    
class Randomizer:
    
    def __init__(self, random_state):
        seed(random_state)
        
    def create_random_location(self):
        x = randint(MAP_BOUNDARIES.x[0], MAP_BOUNDARIES.x[1])
        y = randint(MAP_BOUNDARIES.y[0], MAP_BOUNDARIES.y[1])
        return Location(x, y)


class Player:
    
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
        self._location = location
        self._moves = ['left', 'right', 'up', 'down']
    
    def  __repr__(self):
        return f'Hunter at [{self._location.x}, {self._location.y}]'

class Prey(Player):
    
    def __init__(self, name: str, location: Location):
        super().__init__(name, location)
        self._moves = ['left', 'right', 'up', 'down', 'pass', 'pass', 'pass']


class PrayList(UserList):
    
    def random_move(self):
        for player in self:
            player.random_move()
    
class Game:
    
    def __init__(self, randomizer):
        self._players = PrayList()
        self.hunter = None
        self._randomizer = randomizer
    
    def add_player(self, player_name):
        new_player = Prey(
            name = player_name,
            location = self._randomizer.create_random_location()
        )
        self._players.append(new_player)
        
    def add_hunter(self):
        self.hunter = Hunter(
            location = self._randomizer.create_random_location()
        )
        
    def show_grid(self):
        for player in self._players:
            print(player)
        print(self.hunter)
        
    def make_move(self):
        print('----------------------------')
        self.hunter.random_move()
        self._players.random_move()
    
def set_game() -> Game:
    global MAP_BOUNDARIES
    MAP_BOUNDARIES = MapBoundaries(x = (0, 100), y = (0, 100))
    
    randomizer = Randomizer(random_state = 1)
    game = Game(randomizer)
    game.add_player(player_name = 'John')
    game.add_player(player_name = 'Helen')
    game.add_hunter()
    
    return game
    
def main():
    game = set_game()

    for _ in range(10):
        time.sleep(0.5)
        game.make_move()
        game.show_grid()
    
    
if __name__ == '__main__':
    main()