import pytest
from app import find_min, count_odds


@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 4, 1, 5], 1),         
    ([-1, -5, 0, 2], -5),        
    ([7], 7),                    
    ([10, 20, 30], 99)           
])
def test_find_min(numbers, expected):
    assert find_min(numbers) == expected



@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4, 5], 3),        
    ([2, 4, 6, 8], 0),           
    ([1, 3, 5, 7], 4)            
])
def test_count_odds(numbers, expected):
    assert count_odds(numbers) == expected

