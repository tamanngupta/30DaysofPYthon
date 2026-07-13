import re

txt= 'I love redbull'
match = re.match('I love', txt, re.I)
print(match)
span = match.span()
print(span)

start, end = span
sub = txt[start:end]
print(sub)

m = 'python is such a goof language. Python is the best '

mat = re.findall('Python|python', m)
print(mat)

n= '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

g = re.sub('%', '', n)
print(g)

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

rege = r'-?\d+'
points = re.findall(rege, text)

print('extracted string =', points)

p = [int(i) for i in points]
print(p)
p.sort()
print(p)

s = 0
t = len(p) - 1

h = p[s] - p[t]
print(f'the value required = {abs(h)}')







def is_valid(variable_name):
    regg = r'^[A-Za-z_][A-Za-z0-9_]*$'
    
    if re.match(regg, variable_name):
        return True
    else:
        return False

print(is_valid('first_name'))   
print(is_valid('first-name'))   
print(is_valid('1first_name'))  
print(is_valid_('firstname'))   