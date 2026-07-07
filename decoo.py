from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



for item in countries:
    print(item)


for name in names:
    print(name)

for num in numbers:
    print(num)


def make_upp(letter):
    return letter.upper()

uppp = map(make_upp, countries)
print(list(uppp))

def to_square(num):
    return num**2

tap = map(to_square, numbers)

print(list(tap))

t = map(make_upp, names)
print(list(t))


def land(country):
    if 'land' in country :
        return True
    else: 
        return False

land_map = filter(land, countries)
print(list(land_map))

def charec(country):
    if len(country) == 6:
        return True
    else: 
        return False

check = filter(charec, countries)
print(list(check))

def ch(country):
    if len(country) >= 6:
        return True
    else: 
        return False

mapp = filter(ch, countries)
print(list(mapp))

def star(country): 
    if country.startswith('E') : 
        return True 
    else: 
        return False 

f = filter(star, countries)
print(list(f))


m = filter(star, list(map(make_upp, countries))) 
print(list(m))


new = list(countries + numbers)

def get_string_lists(item):
    if type(item) == str :
        return True 
    else: 
        return False

g = filter(get_string_lists, new)
print(list(g))

def add(x,y):
    return x + y

p = reduce(add, numbers)
print(p)


def con(accu, current):
    if current == countries[-1]:
        return f"{accu} and {current} are north european countries"
    else: 
        return f'{accu}, {current}'

j = reduce(con, countries)
print(j)