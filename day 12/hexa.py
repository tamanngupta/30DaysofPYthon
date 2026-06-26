import random
import string
def hexa():
    poo = 'abcedf' + string.digits
    unir = ''
    for _ in range(6):
        unir += random.choice(poo)
    return unir

print(f'#{hexa()}')

def rgbc():
    m = range(256)
    return f'({random.choice(m)}, {random.choice(m)}, {random.choice(m)})'
print(rgbc())

def lst():
    blank = []
    m = int(input('enter number of colors:'))
    for _ in range(m):
        nc = rgbc()
        blank.append(nc)
    return blank
print(lst())

def ran(ty, num):
    if ty == rgb:
        m == num
        print(lst())
    else:
        blan = []
        for _ in range(num):
            n = hexa()
            blan.append(n)
        print(blan) 

inu = int(input('enter type:'))
binu = int(input('enter number'))
print(ran(inu, binu))