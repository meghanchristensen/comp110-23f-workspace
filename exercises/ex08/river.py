"""File to define River class."""

__author__ = "730659220"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Defining class river."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day = 0
        self.fish = []
        self.bears = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
    
    def view_river(self):
        """Prints values of river in proper format!"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def check_ages(self):
        """Checks ages."""
        bear_alive: list[Bear] = []
        fish_alive: list[Fish] = []

        for bear in self.bears:
            if bear.age <= 5:
                bear_alive.append(bear)

        for fish in self.fish:
            if fish.age <= 3:
                fish_alive.append(fish)

        self.bears = bear_alive
        self.fish = fish_alive

    def bears_eating(self):
        """Bears eating, if there are at least 5 fish in the river, the bear will eat 3."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3) 
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks hunger of Bears, if their hunger_score is < 0 then they die :( ."""
        bear_fed: list[Bear] = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                bear_fed.append(bear)    
        self.bears = bear_fed
        return None
        
    def repopulate_fish(self):
        """Repopulate fish."""
        for i in range(len(self.fish) // 2 * 4):
            fish_repop: Fish = Fish()
            self.fish.append(fish_repop)
        return None
    
    def repopulate_bears(self):
        """Repopulate bears, if there are 2 bears 1 new bear will be born."""
        for i in range(len(self.bears) // 2):
            bear_repop: Bear = Bear()
            self.bears.append(bear_repop)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river!"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        day: int = 0
        while day <= 6:
            self.one_river_day()
            day += 1
        return None

    def remove_fish(self, amount: int):
        """Removes frontmost fish from list."""
        for i in range(amount):
            self.fish.pop(i)