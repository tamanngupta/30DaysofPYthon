import re

url = input('enter twitter url: ').strip()
matches = re.search(r'(https?://)?(www\.)?x\.com/(.+)', url, re.IGNORECASE) 
if matches:
    print(f'the username is {matches.group(3)}')

#re.sub(pattern you want to look for, what do you wanna replace it with, where do you wanna do that i.e the actual strin, count how many times you wanna do this )
#anytime you're writing regex always remember to use speical charecters with  a back slash eppecially with stuff like urls 
#we add a question mark to have s or not have it, we could have just used the straight line but we cannot always take the more verbose path 
#remember when wanting a striing to be assigned to the special charecter use parentheses, for rg. here for www. if we didnt add parantheses, 0 or 1 would be applied to the w and not to the www i.e the whole expression 
#you have to put question mark or special charecter after the expression you want it to be applied to 

#regex needs to work in steps, ask yourself what should I Need start from simple print simple and work your way step  by step
#if matches means that a match was found 