"""Simple calculator module for the SQA lab."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Return base raised to the given exponent."""
    return base ** exponent


def is_even(number):
    """Return True if the number is even."""
    return number % 2 == 0


def factorial(n):
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def average(numbers):
    """Return the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)
