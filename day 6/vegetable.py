f = ('banana', 'tomato', 'mango')
v = ('cauliflower', 'broccoli', 'eggplant')
food = f + v
print(food)
foo = list(food)
print(foo)

n = len(foo)
foo[(n - 1) // 2 : n // 2 + 1] = []
print(foo)

del food
print(food)