def square_root(num):
    """Calculate the square root with 0.000001 precision"""
    if num == 0:
        return 0, 0  # Handle the edge case for zero immediately.

    num = abs(num)

    # Set initial low and high bounds
    low = 0
    high = max(1, num)  # Ensure high is at least 1 for numbers less than 1

    accuracy = 0.000001  # Desired precision
    iteration_count = 0

    while (high - low) > accuracy:  # Continue until the range is within the desired precision
        # Calculate the new guess for the midpoint
        middle = (high + low) / 2
        middle_squared = middle * middle  # Calculate square of the midpoint

        # Adjust bounds based on the squared guess
        if middle_squared > num:
            high = middle  # Middle was too high, adjust high
        else:
            low = middle  # Middle was too low, adjust low

        iteration_count += 1

    # Return the value rounded explicitly to 4 decimal places, as required
    return float(f"{(high + low) / 2:.4f}"), iteration_count

# Testing code
print(square_root(9))        # Expected output: (3.0, some_iteration_count)
print(square_root(25))       # Expected output: (5.0, some_iteration_count)
print(square_root(0.25))     # Expected output: (0.5, some_iteration_count)
print(square_root(10))       # Expected output: (3.1623, some_iteration_count)