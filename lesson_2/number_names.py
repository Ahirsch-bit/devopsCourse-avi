from enum import IntEnum


class number_name(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

def number_converter(x):
    print(number_name(x).name)