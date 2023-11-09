"""Unit test of dictionary functions."""

__author__ = "730659220" 


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
import pytest


def test_invert_easy() -> None:
    """Switches key and value in a dictionary apple:cat to cat:apple!"""
    invert_dict: dict[str, str] = {"apple": "cat"}
    assert invert(invert_dict) == {"cat": "apple"}


def test_invert_harder() -> None:
    """Switches key and value in dictionary, american:flag -> flag: american, dog:cat -> cat:dog, school:escuela -> escuela:school!"""
    invert_dict: dict[str, str] = {"american": "flag", "dog": "cat", "school": "escuela"}
    assert invert(invert_dict) == {"flag": "american", "cat": "dog", "escuela": "school"}


def test_invert_repeat() -> None:
    """Edge case: When repeating keys/values raises KeyError!"""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_favorite_color_blue() -> None:
    """When given dictionary should return blue!"""
    fav_color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(fav_color) == "blue"


def test_favorite_color_pink() -> None:
    """When given dictionary should return pink!"""
    fav_color: dict[str, str] = {"Jill": "blue", "Jack": "pink", "Jennifer": "green", "Barbie": "pink"}
    assert favorite_color(fav_color) == "pink"


def test_favorite_color_blue_green() -> None:
    """Edge case: When given dictionary of tie should return first color which is blue!"""
    fav_color: dict[str, str] = {"Jill": "blue", "Jack": "green", "Jennifer": "green", "Barbie": "blue"}
    assert favorite_color(fav_color) == "blue"


def test_count_groceries_single() -> None:
    """When given list of groceries, will return count of items, will be one for each."""
    new_items: list[str] = {"eggs", "milk", "bread", "creamer"}
    assert count(new_items) == {"eggs": 1, "milk": 1, "bread": 1, "creamer": 1}


def test_count_groceries_multiple() -> None:
    """When given list of groceries, will return count of items, will be multiples."""
    new_items: list[str] = {"milk", "cheese", "creamer", "lettuce", "cheese"}
    assert count(new_items) == {"milk": 1, "cheese": 2, "creamer": 1, "lettuce": 1}


def test_count_groceries_doubles() -> None:
    """When given list of groceries, will return count of items, will be one for each."""
    new_items: list[str] = {"eggs", "milk", "eggs", "bread", "milk", "bread"}
    assert count(new_items) == {"eggs": 2, "milk": 2, "bread": 2}


def test_alphabetizer_1() -> None:
    """When given list of words returns dict with first letter then words that match."""
    words: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(words) == {"c": ["cat", "car"], "a": ["apple", "angry"], "b": ["boy", "bad"]}


def test_alphabetizer_2() -> None:
    """When given list of words returns dict with first letter then words that match."""
    words: list[str] = ["bag", "cat", "bat", "rat", "rug", "car"]
    assert alphabetizer(words) == {"c": ["cat", "car"], "r": ["rat", "rug"], "b": ["bag", "bat"]}


def test_alphabetizer_3() -> None:
    """Edge case: When given list of words returns dict, doesn't reapeat first letter of words."""
    words: list[str] = ["bag", "cat", "rat"]
    assert alphabetizer(words) == {"c": ["cat"], "r": ["rat"], "b": ["bag"]}


def test_update_attendance_present() -> None:
    """When given multiple dicts of students present, combines to form one master list."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday", "Wednesday"
    name: str = "Vrinda", "Caleb"
    assert update_attendance(attendance_log, day, name) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}


def test_update_attendance_present2() -> None:
    """When given multiple dicts of students present, combines to form one master list."""
    attendance_log: dict[str, list[str]] = {"Tuesday": ["Jack", "Kaleb"], "Wednesday": ["Keylly"]}
    day: str = "Tuesday", "Thursday"
    name: str = "Jack", "Matt"
    assert update_attendance(attendance_log, day, name) == {'Tuesday': ['Jack', 'Kaleb'], 'Wednesday': ['Kelly', 'Jack'], 'Thursday': ['Matt']}


def test_update_attendance_present3() -> None:
    """When given multiple dicts of students present, combines to form one master list."""
    attendance_log: dict[str, list[str]] = {"Friday": ["Vrinda", "Kaleb"], "Sunday": ["Alyssa"]}
    day: str = "Sunday", "Wednesday"
    name: str = "Vrinda", "Caleb"
    assert update_attendance(attendance_log, day, name) == {'Friday': ['Vrinda', 'Kaleb'], 'Sunday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}