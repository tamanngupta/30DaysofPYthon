import re

name = input('whats your name? ').strip()
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(name)
#when you use () is going to be a return value, it can extraxt from the user input and capture it : it gives u it back 
# in re.search in location 0 something else will be documented, so here the first charecter or grouping is 1 

#the walrus operator := allows you to assign a value at the same time as asking a boolean question about it 