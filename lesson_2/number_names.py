from enum import IntEnum


class number_name(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
import inflect
def convert(x):
    p = inflect.engine()
    print(p.number_to_words(x))

def number_converter(x):
    try:
        print(number_name(x).name)
    except:
        print("That number doesn't exist in our lists.")