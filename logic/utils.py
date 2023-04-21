from logic.cells import Cell, Ball
from logic.settings import Settings

levels = {
    1: "levels/level_01.txt",
    2: "levels/level_02.txt"
}


def read_level():
    level_file = levels.get(Settings.level_number)

    with open(level_file, 'r') as f:
        lines = f.readlines()

    cells = []
    balls_count = 0
    for i in range(len(lines)):
        cells.append([])
        for elem in lines[i].strip().split(' '):
            cur_cell = Cell.from_string(elem)
            if cur_cell.__class__ == Ball:
                balls_count += 1

            cells[i].append(Cell.from_string(elem))

    return balls_count, cells
