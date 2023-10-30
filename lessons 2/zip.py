"""Combining two lists into a dictionary!"""

__author__ = "730659220"


def zip(keys: list[str], val: list[int]) -> dict[str, int]:
    """Produces a dictionary."""
    the_dict: dict[str, int] = {}

    if len(keys) != len(val) or len(keys) == 0 or len(val) == 0:
        return the_dict
    
    for idx in range(0, len(keys)):
        the_dict[keys[idx]] = val[idx]
    return the_dict

print(zip(["Happy", "Tuesday"], [1, 2]))