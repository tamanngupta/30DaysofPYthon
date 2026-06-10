from sympy import symbols, Eq, solve

x,y = symbols ('x,y')
eq = Eq(y,x**2 + 6*x +9)

zero = solve(eq.subs(y,0),x)[0]
print(f"the zero of the poynomial is {zero}")

p= len('python')
d = len('dragon')
print(p>d)

print('jargon' in 'i hope this course isnt jargon')
print('on' in 'python' and 'dragon')

m = len('python')
print(float(m))
print(str(m))