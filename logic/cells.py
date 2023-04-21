class Cell:

    @staticmethod
    def from_string(str):
        info = str.strip().split('_')

        if info[0] == "ball":
            return Ball(int(info[1]))
        elif info[0] == "wall":
            return Wall(0)
        elif info[0] == "gate":
            return Wall(int(info[1]))
        else:
            return Cell()

    def __str__(self):
        return "empty"


class Ball(Cell):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "color={}".format(self.color)


class Wall(Cell):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "color={}".format(self.color)
