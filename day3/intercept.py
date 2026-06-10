from sympy import symbols, Eq, solve
#symbol helps define x and y, eq is for seting up equations and solve will do the algenbra

x, y = symbols('x,y')
#x and y have been defined 

eq = Eq(2*x-y,2 )
#defined lhs and rhs 

y_int = solve(eq.subs(x,0),y)[0]
#subs is for substitution it puts 0 wherever x is mentioned

x_int = solve(eq.subs(y,0),x)[0]

print(f"the y intercept is {y_int}")
print(f"the x intercept is{x_int}")
#solve returns a list of numbers if you dont put [0] it returns [2], however putting this makes it return the first item of the list individually which is your answer 

c, d = symbols ('c,d')
eq = Eq(4*x - 6*y,-54)

y_in= solve(eq.subs(x,0),y)[0]
x_in = solve(eq.subs(y,0),x)[0]

print(f"the x intercept is {x_in}")
print(f"the y intercept is {y_in}")
