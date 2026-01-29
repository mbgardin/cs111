# Sand.py

from Particle import Particle


from Particle import Particle


# Sand.py
class Sand(Particle):
    def is_move_ok(self, x, y):
        # Check bounds
        if not (0 <= x < self.grid.width and 0 <= y < self.grid.height):
            return False
        return self.grid[y][x] is None

    def physics(self):
        # Try to move straight down
        if self.is_move_ok(self.x, self.y + 1):
            return (self.x, self.y + 1)

        # Try to move down-left (only if left side is free)
        if self.is_move_ok(self.x - 1, self.y + 1) and self.is_move_ok(self.x - 1, self.y):
            return (self.x - 1, self.y + 1)

        # Try to move down-right (only if right side is free)
        if self.is_move_ok(self.x + 1, self.y + 1) and self.is_move_ok(self.x + 1, self.y):
            return (self.x + 1, self.y + 1)

        # If no valid moves, return None
        return None

    def move(self):
        new_position = self.physics()
        if new_position is None:
            return

        # Clear old position
        self.grid[self.y][self.x] = None

        # Update position
        self.x, self.y = new_position

        # Set new position in grid
        self.grid[self.y][self.x] = self
