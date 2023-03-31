from enum import Enum


# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# functional syntax
Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print (Color.BLUE)
centro = 1
if centro:
    print (Color)