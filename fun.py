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

print(c(['man', 'ewe']))

def addl(item, lt):
    insert.lt(0,item)
    return lt

food = ['e','re', 'ew']
print(food_stuff ='tooth', food)