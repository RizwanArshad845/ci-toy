"""Tiny module for the GitHub Actions toy (Task 6.6)."""


def add(a, b):
    return a + b  # fixed: second CI run is green


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
