import random

# Q1: in_range1 function
def in_range1(n):
    """Checks if n is within the range of 1-100 and returns False if not"""
    return 1 <= n <= 100

# Q2: in_range2 function
def in_range2(n):
    """Raises a ValueError if n is not between 1 and 100 inclusive"""
    if not (1 <= n <= 100):
        raise ValueError(f"Value {n} is out of range (1-100).")

# Main function to test the random number generation for Q1 and Q2
def main():
    # Q1: Generate 1000 random numbers and check with in_range1
    print("Testing in_range1 with random numbers:")
    for _ in range(1000):
        num = random.randint(1, 101)
        if not in_range1(num):
            print(f"Number {num} is out of range.")

    # Q2: Generate 1000 random numbers and handle ValueError with in_range2
    print("\nTesting in_range2 with random numbers:")
    for _ in range(1000):
        num = random.randint(1, 101)
        try:
            in_range2(num)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
