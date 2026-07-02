numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
nums = [i for i in numbers if i<0 or i == 0 ]
print(nums)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


n = [num for rows in list_of_lists for num in rows]
print(n)

t = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
for row in t:
    print(row)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Order matters: Outer loop first, then inner loop
output = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

print(output)

players = [[('Lionel Messi', 'Inter Miami', 'Argentina')], [('Cristiano Ronaldo', 'Al Nassr', 'Portugal')], [('Erling Haaland', 'Manchester City', 'Norway')]]
out = [[name.upper(), team[:3].upper(), country.upper()] for sub in players for name,team,country in sub]
print(out)

dic = [{'country': con.upper(), 'city':cit.upper()} for sublist in countries for con,cit in sublist]
print(dic)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
p = [fn + " " + bn for sub in names for fn,bn in sub]
print(p)


slope = lambda ab1, ab2, or1, or2 : (or2 - or1 )/( ab2 - ab1)
print(slope(3,4,5,6))