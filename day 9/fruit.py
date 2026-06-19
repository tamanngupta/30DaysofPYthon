fruits = ['banana', 'orange', 'mango', 'lemon']

f = str(input('enter any fruit:'))
if f in fruits :
    print('given fruit is already in the list')
else:
    fruits.insert(0,f )
    print(fruits)
