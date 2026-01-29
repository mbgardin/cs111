def filter(lst, cond):
    """Returns a list where each element is an element where `cond(elem)` returns `True`.
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> is_even = lambda x : x % 2 == 0
    >>> filter(nums, is_even)
    [2, 4, 6, 8, 10]
    """
    return [elem for elem in lst if cond(elem)]


def print_cond(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> print_cond(5)(is_even)
    2
    4
    """

    def inner(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)

    return inner


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)
    2
    >>> count_factors(4)
    3
    >>> count_factors(12)
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)
    1
    >>> count_primes(3)
    2
    >>> count_primes(20)
    8
    """

    def count(n):
        count = 0
        for i in range(1, n + 1):
            if condition(n, i):
                count += 1
        return count

    return count


class PrintN:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        if self.n > 1:
            print(x)
            return PrintN(self.n - 1)
        elif self.n == 1:
            print(x)
            return PrintN(0)
        else:
            print("done")
            return self

    def __repr__(self):
        return "<function inner_print>"

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    return PrintN(n)




# Helper functions for make_repeater
def increment(x):
    return x + 1


def triple(x):
    return x * 3


def square(x):
    return x * x


def make_repeater(func, n):
    """Return the function that computes the nth application of func.
    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1)
    243
    >>> make_repeater(square, 2)(5)
    625
    >>> make_repeater(square, 4)(5)
    152587890625
    >>> make_repeater(square, 0)(5)
    5
    """
    if n == 0:
        return lambda x: x
    return lambda x: make_repeater(func, n - 1)(func(x))
