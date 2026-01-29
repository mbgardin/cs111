from Grid import Grid
import random


def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def random_rocks(grid, chance_of_rock):
    '''Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''

    # Create a copy of the grid to avoid modifying the original
    new_grid = grid.copy()

    # Loop through each position in the grid row by row (left to right, top to bottom)
    for y in range(grid.height):
        for x in range(grid.width):
            # Only add a rock if the position is empty
            if new_grid.get(x, y) is None:
                if random.random() <= chance_of_rock:
                    new_grid.set(x, y, 'r')

    return new_grid


def random_bubbles(grid, chance_of_bubbles):
    '''Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''

    # Create a copy of the grid to avoid modifying the original
    new_grid = grid.copy()

    # Loop through each position in the grid row by row (left to right, top to bottom)
    for y in range(grid.height):
        for x in range(grid.width):
            # Only add a bubble if the position is empty
            if new_grid.get(x, y) is None:
                if random.random() <= chance_of_bubbles:
                    new_grid.set(x, y, 'b')

    return new_grid


def modify_grid(grid, func, prob):
    '''Take in a grid, a function, and a probability, and
    applies the function to the grid based on the probability.'''

    # Loop through each position in the grid row by row
    for y in range(grid.height):
        for x in range(grid.width):
            # Apply the function if the position is empty and the random chance is met
            if grid.get(x, y) is None:
                if random.random() <= prob:
                    func(x, y)

    return grid

def bubble_up(grid, x, y):
    """
    Move the bubble at (x, y) one row up if possible.
    """

    # Make a copy of the grid to ensure purity
    new_grid = grid.copy()

    # Check if moving the bubble up is possible
    if y > 0 and new_grid.get(x, y - 1) is None:
        new_grid.set(x, y - 1, 'b')  # Move bubble up
        new_grid.set(x, y, None)  # Clear the old spot

    return new_grid


def move_bubbles(grid):
    """
    Move all the bubbles up one row if possible.
    """

    # Make a copy of the grid to ensure purity
    new_grid = grid.copy()

    # Loop over the grid and find bubbles
    for x in range(grid.width):
        for y in range(1, grid.height):  # Start from the second row
            if new_grid.get(x, y) == 'b':
                new_grid = bubble_up(new_grid, x, y)

    return new_grid


def animate_grid(grid, delay):
    """Given a Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        new_grid = move_bubbles(prev)
        if new_grid == prev:
            break
        prev = new_grid
        count += 1
