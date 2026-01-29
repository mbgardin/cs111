class Grid:
    def __init__(self, width, height):
        # Initialize the grid with given width (number of columns) and height (number of rows)
        self.height = height  # Number of rows
        self.width = width    # Number of columns
        self.array = [[None for _ in range(width)] for _ in range(height)]

    @staticmethod
    def check_list_malformed(lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list.")
        if len(lst) == 0:
            raise ValueError("Input list cannot be empty.")
        for row in lst:
            if not isinstance(row, list):
                raise ValueError("All elements of the input list must also be lists.")
        row_length = len(lst[0])
        for row in lst:
            if len(row) != row_length:
                raise ValueError("All rows must have the same length.")

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        new_grid = Grid(width, height)
        from copy import deepcopy
        new_grid.array = deepcopy(lst)
        return new_grid

    def copy(self):
        return Grid.build(self.array)

    def __repr__(self):
        return f"Grid.build({repr(self.array)})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        return False

    def __str__(self):
        # Update here to ensure the dimensions are printed as (height, width)
        first_value = self.array[0][0] if self.height > 0 and self.width > 0 else None
        return f"Grid({self.height}, {self.width}, first = {first_value})"

    def get(self, col, row):
        # Get the value at a specific position in the grid
        if self.in_bounds(col, row):
            return self.array[row][col]
        raise IndexError("Index out of bounds.")

    def set(self, col, row, value):
        # Set the value at a specific position in the grid
        if self.in_bounds(col, row):
            self.array[row][col] = value
        else:
            raise IndexError("Index out of bounds.")

    def in_bounds(self, col, row):
        # Check if a given position is within the bounds of the grid
        return 0 <= row < self.height and 0 <= col < self.width

# Example Usage:
if __name__ == "__main__":
    try:
        # Testing `check_list_malformed`
        Grid.check_list_malformed([[2, 1], [55, 55, 55, 55]])  # Should raise ValueError
    except ValueError as e:
        print(f"ValueError: {e}")

    # Testing `build` method
    grid = Grid.build([[5, 4, 3, 3, 4], [4, 1, 5, 2, 2]])
    print(repr(grid))  # Should print: Grid.build([[5, 4, 3, 3, 4], [4, 1, 5, 2, 2]])

    # Testing `copy` method
    copy_grid = grid.copy()
    print(repr(copy_grid))  # Should print the same as `grid`

    # Testing `__eq__` method with a list
    grid2 = [[1, 1, 1], [2, 3, 5]]
    print(grid == grid2)  # Should print: False

    # Testing `__eq__` method with another Grid object
    grid3 = Grid.build([[5, 4, 3, 3, 4], [4, 1, 5, 2, 2]])
    print(grid == grid3)  # Should print: True