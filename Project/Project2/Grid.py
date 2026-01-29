from copy import deepcopy


class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None for i in range(self.width)] for j in range(self.height)]

    def in_bounds(self, x, y):
        if (x < self.width and y < self.height) and (x >= 0 and y >= 0):
            return True
        else:
            return False

    def get(self, x, y):
        if self.in_bounds(x, y):
            return (self.array[y][x])
        else:
            raise IndexError("Invalid Bounds")
            return

    def set(self, x, y, val):
        if self.in_bounds(x, y):
            self.array[y][x] = val
            return None
        else:
            raise IndexError("Invalid Bounds")
            return

    @staticmethod
    def check_list_malformed(lst):

        if not isinstance(lst, list):
            raise ValueError("Not a list")
        if len(lst) == 0:
            raise ValueError("Needs full list")
        for x in lst:
            if not isinstance(x, list):
                raise ValueError("Must have lists inside list")
            if not len(x) == len(lst[0]):
                raise ValueError("All elements must be the same length")

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        myGrid = Grid(width, height)
        myGrid.array = deepcopy(lst)
        return myGrid

    def copy(self):
        return Grid.build(self.array)

    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid.build({self.array})'

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other
        elif isinstance(other, list):
            return self.array == other
        else:
            return False