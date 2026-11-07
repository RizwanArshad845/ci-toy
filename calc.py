"""Tiny module for the GitHub Actions toy (Task 6.6)."""


def add(a, b):
    return a - b  # deliberate bug: makes the first CI run fail (red)


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
