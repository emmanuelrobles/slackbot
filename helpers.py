def chance(num):
    from random import randrange
    if randrange(0, 100) < num:
        return True
    return False
