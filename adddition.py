```python
"""
File: addition.py
Description: This module defines a function, add_numbers, to add two numbers together.
             It includes error handling for invalid input types, ensuring both inputs
             are either integers or floats.  The function returns the sum of the two
             numbers, or None if an error occurs.
"""


def add_numbers(x, y):
    """
    Adds two numbers together.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
        Returns None if either x or y is not a number (int or float).

    Raises:
        TypeError: If either x or y is not a number.
    """
    try:
        x = float(x)  # Attempt to convert to float to handle integers and floats
        y = float(y)
        return x + y
    except ValueError:
        print("Error: Both inputs must be numbers (integers or floats).")
        return None  # Or raise a TypeError if you prefer strict type checking


if __name__ == "__main__":
    """
    Example usage of the add_numbers function.
    """
    # Example 1: Adding two integers
    num1 = 5
    num2 = 3
    sum_result = add_numbers(num1, num2)
    if sum_result is not None:
        print(f"The sum of {num1} and {num2} is: {sum_result}")

    # Example 2: Adding an integer and a float
    num3 = 10
    num4 = 2.5
    sum_result = add_numbers(num3, num4)
    if sum_result is not None:
        print(f"The sum of {num3} and {num4} is: {sum_result}")

    # Example 3: Handling invalid input (string)
    num5 = "hello"
    num6 = 7
    sum_result = add_numbers(num5, num6)
    if sum_result is not None:
        print(f"The sum of {num5} and {num6} is: {sum_result}")  # This line will not execute because add_numbers returns None

    # Example 4: Adding two negative numbers
    num7 = -5
    num8 = -2
    sum_result = add_numbers(num7, num8)
    if sum_result is not None:
        print(f"The sum of {num7} and {num8} is: {sum_result}")
```