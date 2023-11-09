"""C0Q07."""

from __future__ import annotations

__author__ = 730659220


class Point:
    """Practicing Object Oriented Programming."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that multiplies x and y values by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method that creates a new Point rather than mutating it."""
        n_x = self.x * factor
        n_y = self.y * factor
        return Point(n_x, n_y)