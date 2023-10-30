"""Test my zip function!"""

__author__ = 730659220

from lessons.zip import zip


def test_empty_dict() -> None:
    """Zip of an empty list should retun {}."""
    keys: list[str] = []
    val: list[int] = []
    assert zip(keys, val) == {}


def test_dict_two_items() -> None:
    """Zip of a list of two should return {"Happy": 11, "Birthday": 2}."""
    keys: list[str] = ["Happy", "Birthday"]
    val: list[int] = [11, 2]
    assert zip(keys, val) == {"Happy": 11, "Birthday": 2}


def test_dict_three_items() -> None:
    """When inputting three separate keys and val variables, a dict should be returned {"Green": 1, "Yellow": 6, "Blue": 10}."""
    keys: list[str] = ["Green", "Yellow", "Blue"]
    val: list[int] = [1, 6, 10]
    assert zip(keys, val) == {"Green": 1, "Yellow": 6, "Blue": 10}