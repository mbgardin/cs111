class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            print("Error: Coordinates out of bounds.")
            return None

    def set(self, x, y, val):
        if self.in_bounds(x, y):
            self.array[y][x] = val
        else:
            print("Error: Coordinates out of bounds.")

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.array == other.array
