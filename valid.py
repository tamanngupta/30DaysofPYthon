import re

email = input('whats your email?: ').strip()
#re.search(what to find, where to find, what to flag)
#  . is any charecter except a new line, * 0 or more repetition, + 1 or more repetitions, ? 0 or 1 repetition, this is for how many times you want a specific charecter to repeat eg/ {m} means m repetitions of say digits 

if re.search(r"^(\w|\.)a+@(\w+\.)?\w+\.(edu|org|com)$", email, re.IGNORECASE):
    print('valid')
else: 
    print('invalid ')

#re.IGNORECASE  - allows u to ignore the case or be case insensitive without actually changing the variable value 
#. right now cannot be accepetd after @ and before .  but technically there could be other email addressess

print('shit I dont wanna miss today')