"""Practice with dictionary functions!"""

__author__ = 730659220


def invert(invert_dict: dict[str, str]) -> dict[str, str]:
    """Swaps position of key and value inputted."""
    dictionary: dict[str, str] = {}
    for elem in invert_dict:
        new_key: str = invert_dict[elem]
        if new_key in dictionary:
            raise KeyError("You cannot use the same key twice!")
        dictionary[new_key] = elem
    return dictionary


def favorite_color(fav_color: dict[str, str]) -> str:
    """Returns most liked color from list of people's preferences!"""
    best_color: str = ""
    count: int = 0
    color_list: dict[str, int] = {}
    for color in fav_color:
        if fav_color[color] in color_list:
            color_list[fav_color[color]] += 1
        else:
            color_list[fav_color[color]] = 1
    for color in color_list:
        if color_list[color] > count:
            count = color_list[color]
            best_color = color
    return best_color


def count(new_items: list[str]) -> dict[str, int]:
    """When a list is entered, a dictionary is created with a count of each item."""
    result_dict: dict[str, int] = {}
    for item in new_items:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """When a list is entered, the first letter of each word is saved and words that start with that are provided in a dictionary."""
    abc_dict: dict[str, list[str]] = {}
    for word in words:
        if word[0]:
            first_let = word[0].lower()
            if first_let in abc_dict:
                abc_dict[first_let].append(word)
            else:
                abc_dict[first_let] = [word]
    return abc_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """When given attendence logs, a master list will be printed."""
    if day in attendance_log and name not in attendance_log[day]:
        attendance_log[day].append(name)
    else:
        attendance_log[day] = [name]
    return attendance_log