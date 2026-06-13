lst =[]
ls = [43,32423,543,23,54]
print(len(ls))
first = ls[0]
second = ls[1]
thirf = ls[2]
print(first, second, thirf)


mixed_data_types = ['tamanna', 18, '6 foot', 'single as a pringle ', 'earth']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
f = it_companies[0]
l = it_companies[int(len(it_companies)- 1 )]
m = it_companies[int((len(it_companies)+1)/2)]
print(f, l, m)

it_companies[0] = 'me'
print(it_companies)

it_companies.append('me')
print(it_companies)

it_companies.insert(4,'tesla')
print(it_companies)

it_companies[3] = 'APPLE'
print(it_companies)

bash = ["#"]
print(it_companies + bash)

print('Facebook' in it_companies)

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

st = it_companies[5:]
print(st)

ms = it_companies[0:7]
print(ms)

del it_companies[0]
print(it_companies)

del it_companies[4]
print(it_companies)

del it_companies[int(len(it_companies)-1)]
print(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
sr =front_end + back_end
print(front_end + back_end)
sm = sr.copy()
li = ['python', 'sql']
print(li + sm )