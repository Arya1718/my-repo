```python
import math

def find_factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    The factorial of a non-negative integer 'n', denoted by n!, is
    the product of all positive integers less than or equal to n.
    For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
    The factorial of 0 (0!) is defined as 1.

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers. 'n' must be a non-negative integer.")

    if n == 0:
        return 1
    
    # Using an iterative approach for efficiency and to avoid recursion depth limits
    # for potentially large n.
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
        
    return factorial_result

```