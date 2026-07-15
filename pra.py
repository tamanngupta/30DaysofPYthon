def fact(x):
    if x == 0:
        return 1 

    else: 
        return x * fact(x-1)

print(fact(7))


m = int(input('enter your number: '))
lst = [{i: i*i} for i in range(1,m)]

print(lst)