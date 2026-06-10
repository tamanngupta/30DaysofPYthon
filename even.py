num = int(input('enter number'))
if num % 2 == 0 :
    print(f'{num} is even')

else:
    print(f'{num } is odd')


num1 = 7//3
num2 = int(2.7)
print(num1 == num2)

t = type(10)
g = type('10')
print(t==g)

b = int(9.8)
print(b == 10)

hours = float(input('enter hours:'))
pay = float(input('enter rate per hour:'))
tp = hours * pay
print(f"total pay is {tp}")

y = int(input('enter the number of years you have lived for:'))
time = y * 3600 * 24 * 365
print(f"you have lived for {time} seconds")

for n in range(1,6):
    print(1, n , n**2, n**3)