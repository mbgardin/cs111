def digit_counter(func, num):
    """Return the number of digits when func(num) is true"""
    counter = 0

    print(f"DEBUG: Starting digit_counter with num = {num}")  # Track input

    while num > 0:  # Fix condition to avoid an infinite loop when num = 0
        digit = num % 10
        print(f"DEBUG: tmp = {digit}")  # Debug current digit

        if func(digit):
            counter += 1
            print(f"DEBUG: i = {counter}")  # Debug when counter is incremented

        num = num // 10
        print(f"DEBUG: Updated num = {num}")  # Track the value of num after dividing

    print(f"DEBUG: Final counter value = {counter}")  # Track the result
    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


# Testing the digit_counter function with different numbers
print("DEBUG: Test 1 - Counting even digits in 123456")
result = digit_counter(is_even, 123456)
print(f"Result: {result}\n")

print("DEBUG: Test 2 - Counting even digits in 1112")
result = digit_counter(is_even, 1112)
print(f"Result: {result}\n")

print("DEBUG: Test 3 - Counting even digits in 0")
result = digit_counter(is_even, 0)
print(f"Result: {result}\n")

print("DEBUG: Test 4 - Counting even digits in 24680")
result = digit_counter(is_even, 24680)
print(f"Result: {result}\n")