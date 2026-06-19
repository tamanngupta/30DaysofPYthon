age = int(input('enter your age:'))
if age >= 18 :
    print('You are old enough to drive')
else:
    print(f"you have to wait {18-age} years")


your_age = int(input('enter your age:'))
my_age = 18 

if your_age > my_age and your_age - my_age == 1 :
    print('you are one year older than me')

elif your_age > my_age :
    print(f"you are {your_age - my_age} years older than me")

elif your_age < my_age and my_age - your_age == 1 :
    print('you are 1 year younger than me ')

else: 
    print(f"you are {my_age - your_age} years younger than me ")