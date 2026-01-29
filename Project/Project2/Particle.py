class Particle:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y
        self.width = grid.width
        self.height = grid.height

    def move(self):
        self.whereToMove = self.physics()
        if self.whereToMove is None:
            return
        else:
            self.item = self.get(self.x, self.y)
            self.set(self.whereToMove[0], self.whereToMove[1], self)
            self.set(self.x, self.y, None)
            self.x, self.y = self.whereToMove  # Update the coordinates

    def get(self, x, y):
        return self.grid.get(x, y)

    def set(self, x, y, val):
        return self.grid.set(x, y, val)

    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"