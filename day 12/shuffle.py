import random
import string

def shuffle_list(lit):
    random.shuffle(lit)
    return lit

print(shuffle_list(['me', 'oui', 'we', 'wen']))


def sett():
    me = set()
    c = string.digits
    while len(me)<7:
        t = random.choice(c)
        me.add(t)
    return me

print(sett())