"""File to define Fish class!"""


class Fish:
    """Define class Fish."""

    age: int
    
    def __init__(self):
        """Assigns age to 0."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Raises fish age attribute by 1."""
        self.age += 1
        return None