"""File to define Bear class!"""


class Bear:
    """Defines class Bear."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Assigned age and hunger score."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Increases value of age atrribute by 1!"""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Update bear's hunger_score to equal num_fish."""
        self.hunger_score = num_fish
        return None