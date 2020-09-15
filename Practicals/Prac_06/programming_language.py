"""CP1404 practical intermediate"""


class ProgrammingLanguage:
    """store programming languages"""
    def __init__(self, name, typing, reflection, year):
        """Create programming language from the values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Is language dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string of ProgrammingLanguage"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
