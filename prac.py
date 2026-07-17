
lst = []

for i in range(2000, 3200):
    if i%7  == 0 and i%5 !=0: 
        lst.append(i)

print(lst)





def accepting_lists(strr):
    m = strr.split(',')

    lst = []
    for i in m: 
        lst.append(i)

    return lst, tuple(lst)

print(accepting_lists('43,5432,5423,32,21,32'))