from operator import add, mul
import math

# Q1: Product and Summation
def product(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be an integer greater than or equal to 1.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def summation(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be an integer greater than or equal to 0.")
    return sum(range(1, n + 1))

# Q2: Statistics Functions
def mean(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list.")
    return sum(data) / len(data)

def median(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list.")
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def mode(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list.")
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    max_freq = max(frequency.values())
    for value, count in frequency.items():
        if count == max_freq:
            return value

def standard_deviation(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list.")
    μ = mean(data)
    variance = sum((x - μ) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# Stat Analysis - Run all stats on the data and return a dictionary
def stat_analysis(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list.")
    return {
        "mean": mean(data),
        "median": median(data),
        "mode": mode(data),
        "std_dev": standard_deviation(data)
    }

# Q3: Refactored Product and Summation using Accumulate
def accumulate(merger, initial, n):
    if not isinstance(n, int) or n < initial:
        raise ValueError("Input must be an integer greater than or equal to initial.")
    total = initial
    for i in range(1, n + 1):
        total = merger(total, i)
    return total

def product_short(n):
    return accumulate(mul, 1, n)

def summation_short(n):
    return accumulate(add, 0, n)

# Q4: Invert and Change Functions
def invert(x, limit):
    if x == 0:
        raise ZeroDivisionError("Division by zero.")
    result = 1 / x
    return result if result < limit else limit

def change(x, y, limit):
    if x == 0:
        raise ZeroDivisionError("Division by zero.")
    result = abs(y - x) / x
    return result if result < limit else limit

# Q5: Refactored Invert and Change using Limited
def limited(numerator, denominator, limit):
    if denominator == 0:
        raise ZeroDivisionError("Division by zero.")
    result = numerator / denominator
    return result if result < limit else limit

def invert_short(x, limit):
    return limited(1, x, limit)

def change_short(x, y, limit):
    return limited(abs(y - x), x, limit)
