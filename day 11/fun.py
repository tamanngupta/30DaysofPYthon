def sum_of_2_numbers(num1,num2):
    total = num1 + num2
    return total 
print(sum_of_2_numbers(23,42))

def area(radius):
    ar = 3.14 * radius * radius 
    return ar
print(f"area of the circle with radius 7 is {area(7)}")

def add_all_nums(*nums): 
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "error"
    return(total)

print(add_all_nums(3242,4234,11341,543))

def convert(temp):
    far = temp*(9/5) + 32
    return far
print(convert(78))

def season(month):
    if month in ['Feb', 'Jan', 'Dec']:
        return 'winter'
    elif month in ['March', 'April', 'may']:
        return 'spring'
    elif month in ['August', 'June', 'July']:
        return 'summer'
    elif month in ['November', 'december', 'October']:
        return 'autumn'
    else:
        return 'invalid'
print(season('Jan'))

def slope(x1, x2, y1, y2):
    slo = (y2-y1)/(x2-x1)
    return slo
print(slope(32,43,43,21))

def quad(a,b,c):
   t = ((-1*b)+ ((b**2)-4*a*c))/(2*a)
   m = ((-1*b)-((b**2)-4*a*c))/(2*a)
   return t, m
print(quad(1,5,6,))


def reverse_list(lst):
    reversed_list = []

    for item in lst:
        reversed_list.insert(0,item)
    return reversed_list

print(reverse_list([312,42,42,21]))

def c(l):
    cap =[]
    for item in l:
        t = item.capitalize()
        cap.insert(0,t)
    return cap

def add_item(lst, item):
    lst.append(item)
    return lst
li = [424,42,43,2]
print(add_item(li, 422))

def sum_num(*num):
    tota = 0 
    for item in num:
        tota += item
    return tota

print(sum_num(42,46,32))

def sum_of_odds(*nums):
    tot = 0 
    for it in nums:
        if it%2 == 0:
            continue
        else:
            tot += it
    return(tot)

print(sum_of_odds(423,346,12,34,76))


def sum_of_even(numa):
    tpt = 0
    for ite in numa:
        if ite % 2 == 0 :
            tpt += ite
        else:
            continue
    return (tpt)

print(sum_of_even(range(0,10)))

def counte(*n):
    ls =[]
    lt= []
    for num in n :
        if num%2 == 0:
            ls.insert(0,num)
        else:
            lt.insert(0,num)
    return len(ls), len(lt)

print(counte(43,23124,56,7,4324342,))

def factorial(nu):
    if nu == 0:
        return 1
    
    t = 1
    for i in range(1,nu+1):
        t *= i
    return t 

print(factorial(6))

def stats(ls):
    tor = 0
    for item in ls:
        tor += item
    mean = tor/(len(ls))
    return mean

print(f"mean is {stats([43,54,322,12])}")

def stat(ls):
    ls.sort()
    if len(ls) % 2 == 0:
        return ls[int(len(ls)/2)], ls[int(len(ls)/2 + 1)]
    else:
        return ls[(len(ls)+1)/2]
print(stat([432,4234,12,32]))

def mode(lt):
    hc = 0
    mv = None
    for item in lt:
        cc = lt.count(item)
        if cc>hc:
            hc = cc        
            mv = item
    return mv
print(mode([42,4313,324,213,213,213]))

def ran(l):
    h = max(l)
    l = min(l)
    rane = h - l
    return rane

print(ran([432,323,231]))

def variance(l):
    t = 0
    m = 0
    for item in l:
        t += item
        m += item**2
        mean = t/(len(l))
    var = (m/(len(l)) - mean**2)
    return var
print(variance([42,342,323,443,1]))

    

def is_prime(num):
    for i in range(2,num):
        if num == 2:
            return '2 is a prime number'
        elif num % i == 0 :
            return f'{num} is a composite number'

        else:
            return f'{num} is a prime number'
print(is_prime(23))

def unique(ls):
    s = set(ls)
    if len(s) == len(ls):
        return 'all items are unique'
    else:
        return 'all items are not unique'
print(unique([432,34,34,43,65]))

def tye(ls):
    fs = type(ls[0])
    for item in ls:
        if type(item) != fs : 
            return ' all data is not of same type'
    return 'all data is of same type'
print(tye([32,'wer', 43.2]))

