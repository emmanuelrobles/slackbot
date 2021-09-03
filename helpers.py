bot_lines = ['hey peeps :fire:', 'what do you need?', 'ohh, do you wanna hear a joke?']
bot_lines_pierre = ['Hey pierre, do you miss me?', 'We gotta talk about Pierre', 'Im calling you after 5']
bot_lines_shh = ['just let it happen', 'watch it burn!!']


def chance(num):
    from random import randrange
    if randrange(0, 100) < num:
        return True
    return False
