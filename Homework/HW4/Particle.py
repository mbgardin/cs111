# Particle.py

class Particle:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"  # No space after commas

    def move(self):
        new_position = self.physics()
        if new_position is None:
            return
        self.grid[self.y][self.x] = None
        self.x, self.y = new_position
        self.grid[self.y][self.x] = self

    def physics(self):
        pass
