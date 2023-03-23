# simplemathExample.py

from inspect import getframeinfo, currentframe
# from ..simplemath import add
from src.simplemath import add

# myname = getframeinfo(currentframe()).function
myname = getframeinfo(currentframe()).function
filename = __file__.split('/')[-1]
# from .. import simplemath

# print(f"{simplemath = }")

print(f"{filename}: {__name__ = }")
print(f"{filename}: {__package__ = }")


def add_demo():
    print('add demo')
    add(7, 4)
