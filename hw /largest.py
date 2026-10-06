def find_largest(numbers: list[int]) -> int:
    """Return the largest element in numbers."""
    largest = numbers[0]
    for value in numbers[1:]:
        if value > largest:
            largest = value
    return largest


numbers = [12, 45, 7, 89, 23]
print(f"Largest element is {find_largest(numbers)}")
