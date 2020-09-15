"""CP1404 practical do it yourself """
CURRENT_YEAR = 2020
VINTAGE = 50


class Guitar:
    """store guitars"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Is the guitar older than 50"""
        return self.get_age() >= VINTAGE
