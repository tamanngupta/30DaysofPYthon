import random 
import string
def user():
    c = string.ascii_lowercase + string.digits
    user_id = ''
    for _ in range(6):
        user_id += random.choice(c)
    return user_id

print(user())

def userr():
    n = int(input('enter number of charecters :'))
    m = int(input('enter number of entries'))

    charecters = string.ascii_lowercase + string.digits
    
    for _ in range(m):
        user_o = ''

        for _ in range(n):
            user_o += random.choice(charecters)
        print(user_o)

userr()

def rgb():
    pool = range(256)
    return f' r is ({random.choice(pool)}) b is {random.choice(pool)} g is {random.choice(pool)}'

print(rgb())

