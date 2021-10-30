import time
import random

class OutOfRange(Exception):
    """ Out of range (0 or 1) """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class Coin():
    def __init__(self):
        self.side = 1
        random.seed(time.time())

    def flip(self):
        self.side = random.randint(0,1)
        return self.side
    
    def set_side(self, side):
        if not (side == 1 or side == 0):
            raise OutOfRange("Out of Range (0 or 1)")
        self.side = side
        return self.side
    
    def get_side(self):
        return self.side