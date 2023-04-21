from enum import Enum

from logic import utils
from logic.cells import Cell, Wall


class Kugeim:
    def __init__(self):
        self.balls_count, self.field = utils.read_level()

    def move_ball(self, r, c, dir):
        ball = self.field[r][c]
        self.field[r][c] = Cell()

        next_r, next_c = 0, 0
        if dir == Direction.UP:
            while self.field[r - 1][c].__class__ == Cell:
                r -= 1
            next_r -= 1
        elif dir == Direction.DOWN:
            while self.field[r + 1][c].__class__ == Cell:
                r += 1
            next_r += 1
        elif dir == Direction.LEFT:
            while self.field[r][c - 1].__class__ == Cell:
                c -= 1
            next_c -= 1
        else:
            while self.field[r][c + 1].__class__ == Cell:
                c += 1
            next_c += 1

        next_r += r
        next_c += c
        next_cell = self.field[next_r][next_c]
        if next_cell.__class__ == Wall and next_cell.color == ball.color:
            print(next_cell.__class__)
            print(next_cell.color == ball.color)
            print(self.balls_count)
            self.balls_count -= 1
            print(self.balls_count)
            self.field[r][c] = Cell()
            if self.balls_count == 0:
                print(self.balls_count)
                return True
        else:
            self.field[r][c] = ball
            return False


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
