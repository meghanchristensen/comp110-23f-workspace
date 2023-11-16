"""C0Q07."""

from __future__ import annotations

__author__ = 730659220


class Point:
    """Practicing Object Oriented Programming."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that multiplies x and y values by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method that creates a new Point rather than mutating it."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Prints values in proper format!"""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplies x and y values by an assigned factor!"""
        mul_point: Point = Point(self.x, self.y)
        mul_point.x *= factor
        mul_point.y *= factor
        return mul_point
    
    def __add__(self, factor: int | float) -> Point:
        """Adds x and y values by an assigned factor!"""
        add_point: Point = Point(self.x, self.y)
        add_point.x += factor
        add_point.y += factor
        return add_point