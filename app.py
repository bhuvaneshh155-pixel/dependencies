def find_min(numbers):
    """Returns the minimum number in a list. Returns None if empty."""
    if not numbers:
        return None
    return min(numbers)

def count_odds(numbers):
    """Counts how many odd integers are in the list."""
    return sum(1 for x in numbers if x % 2 != 0)
