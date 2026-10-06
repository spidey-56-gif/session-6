def calculate_factorial(number: int) -> int:
    """Return the factorial of number."""
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


NUMBER = 5
print(f"Factorial of {NUMBER} = {calculate_factorial(NUMBER)}")
