def find_min(numbers):
    """Returns the lowest value in a list. Returns None if the list is empty."""
    if not numbers:
        return None
    return min(numbers)

def count_odds(numbers):
    """Returns the total count of odd integers present in the list."""
    return sum(1 for x in numbers if x % 2 != 0)
