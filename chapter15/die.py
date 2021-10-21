from random import randint

class Die():
    """To create a class named Die"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = 6
    
    def roll(self):
        """返回一个位于1到6之间的骰子面数的随机值"""
        return randint(1, self.num_sides)