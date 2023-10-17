"""Summing the elements of a list using different loops."""

__author__ = "730659220"


def w_sum(vals: list[float]) -> float:
    """When list of numbers is enter the sum of the numbers is returned."""
    idx: int = 0
    sum_vals: float = 0.0
    while idx < len(vals):
        sum_vals = sum_vals + vals[idx]
        idx += 1
    return sum_vals


def f_sum(vals: list[float]) -> float:
    """When list of numbers is enter the sum of the numbers is returned."""
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """When list of numbers is enter the sum of the numbers is returned."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
