import random


# data processing


# callables

def recover_or_die(person):
    """returns 0 if no change, 1 if recovery today, and 2 if death"""

    draw = 0
    if person.days >= 7:
        draw = random.triangular(0, 5, 3)
        draw = round(draw / 2.5)

    return draw
