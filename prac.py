import random

def check_target(lst):
    target = int(input('enter target: '))
    lstt = list(lst)
    for m,n in lstt:
        if target - m == n and m!=n :
            return lstt.index(m), lstt.index(n)
        else:
            return 'not applicable'

print(check_target([43,5432,65,21]))