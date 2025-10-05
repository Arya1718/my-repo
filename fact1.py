```python
def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    The factorial of a non-negative integer 'n', denoted by n!, is the product
    of all positive integers less than or equal to 'n'.
    For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
    The factorial of 0 is defined as 1 (0! = 1).

    Args:
        n: A non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of the input number 'n'.

    Raises:
        TypeError: If 'n' is not an integer.
        ValueError: If 'n' is a negative integer.
    """
    # Type checking: Ensure the input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    # Value checking: Factorial is not defined for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case: Factorial of 0 is 1
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```