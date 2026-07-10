try:
    print(10+'5')

except Exception as e:
    print(e)

def sum_of(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 3, 54, 43, 454]
print(sum_of(*lst))

args = range[2,7]

print(sum_of(*args))