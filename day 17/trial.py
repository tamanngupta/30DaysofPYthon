try:
    print(10+'5')

except Exception as e:
    print(e)

def sum_of(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 3, 54, 43, 454]
print(sum_of(*lst))


def unpacking_info(name, country, age):
    return f'My name is {name}. I am {age} years old and I live in {country}'

t = {'name': 'Tamanna', 'age': 18, 'country':'India'}

print(unpacking_info(**t))

def sum_all(*args):
    s = 0
    for i in args: 
        s += i
    return s

print(sum_all(54,3223,54))

items = [32,654,321]
for index, item in enumerate(items):
    print(index, item)


fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

fruits_and_vegetables = []
for f, v in zip(fruits, vegetables):
    fruits_and_vegetables.append({'fruit':f, 'vegies':v} )


print(fruits_and_vegetables)


names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

Nordic_countries = names[:4]
print(*Nordic_countries)