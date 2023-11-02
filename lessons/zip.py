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


def favorite_color(fav_color: dict[str, str]) -> str:
    """Returns most liked color from list of people's preferences!"""
    fav_color: dict[str, str] = {}
    color_count = 0
    pop_color: None
    for color in fav_color:
        if color in fav_color:
            color_count[color] += 1
            pop_color = color_count
        else:
            color_count[color] = 1
    return pop_color
print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))

