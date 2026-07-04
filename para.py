def su(nums):
    summ = sum(nums)
    return summ 

def higher_order_function(f, lst):
    summation = f(lst)
    return summation

print(higher_order_function(su, [43,4321,436]))

def square(num):
    sq = num**2
    return sq

def cube(num):
    cue = num**3
    return cue

def sqroot(num):
    sq = num**0.5
    return sq

def ht(type):
    if type == 'square':
        return square
    elif type == 'cube': 
        return cube
    else: 
        return sqroot


result = ht('square')
print(result(3))
result = ht('cube')
print(result(3))


def add_ten():
    ten = 10
    def add(num):
        res = ten + num
        return res
    return add
 
closure = add_ten()
print(closure(5))