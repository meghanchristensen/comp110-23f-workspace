"""EX04 List Utility Functions!"""

__author__ = "730659220"


def all(list: list[int], input_int: int) -> bool:
    """When given a list and a single integer, True or False is returned if the int value matches the entire list."""
    list_idx: int = 0
    if len(list) == 0:
        return False
    while list_idx < len(list):
        if list[list_idx] != input_int:
            return False
        list_idx += 1
    else:
        return True


def max(list_ints: list[int]) -> int:
    """When a list of ints are given, will return the max, if no numbers are given, will raise a ValueError."""
    if len(list_ints) == 0:
        raise ValueError("max() arg is an empty List")
    max_val = list_ints[0]
    x: int = 0
    
    while x <= len(list_ints) - 1:
        if list_ints[x] >= max_val:
            max_val = list_ints[x]
        else:
            max_val = max_val
        x += 1
    return max_val
        

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """When two lists are entered, function will test if each object in list matches order of other list."""
    if list_one == list_two:
        return True
    else:
        return False
    
    