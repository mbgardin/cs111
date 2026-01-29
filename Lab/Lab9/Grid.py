class Grid:
    def __init__(self, width, height):
        """Initializes the grid with given width and height."""
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        """Returns True if the (x, y) position is in bounds of the grid, False otherwise."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        """Gets the value at position (x, y). Raises IndexError if out of bounds."""
        if not self.in_bounds(x, y):
            raise IndexError(f"Coordinates ({x}, {y}) are out of bounds.")
        return self.grid[y][x]

    def set(self, x, y, value):
        """Sets the value at position (x, y). Raises IndexError if out of bounds."""
        if not self.in_bounds(x, y):
            raise IndexError(f"Coordinates ({x}, {y}) are out of bounds.")
        self.grid[y][x] = value


# Example of how the Grid class might be used:
if __name__ == "__main__":
    grid = Grid(3, 3)
    print("Testing in_bounds function:")
    # Testing in bounds
    print(grid.in_bounds(1, 1))  # Should return True
    # Testing out of bounds
    print(grid.in_bounds(3, 3))  # Should return False

    print("\nTesting get and set functions:")
    # Setting and getting a valid value
    grid.set(1, 1, 42)
    print(grid.get(1, 1))  # Should return 42

    # Trying to get and set out of bounds to raise IndexError
    try:
        grid.get(3, 3)
    except IndexError as e:
        print(f"Error: {e}")

    try:
        grid.set(3, 3, 99)
    except IndexError as e:
        print(f"Error: {e}")
