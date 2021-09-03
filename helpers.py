bot_lines = ['hey peeps :fire:', 'what do you need?', 'ohh, do you wanna hear a joke?']
bot_lines_pierre = ['Hey pierre, do you miss me?', 'We gotta talk about Pierre', 'Im calling you after 5']
bot_lines_shh = ['just let it happen', 'watch it burn!!']


def chance(num, fun):
    from random import randrange
    if randrange(0, 100) < num:
        fun()
        return True
    return False
