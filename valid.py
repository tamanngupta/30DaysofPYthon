email = input('whats your email? ').strip()
#strip allows you to ignore any leading whitespaces or ending ones just pure text


username, domain = email.split('@')
#to get a username and domain name 
# you can just define two variables in one single line if you know the kind of value you will get otherwise you can always use a list

if username and domain.endswith('.edu') : #this checks for the presence of a username, a truthee value if you will. It doesn't bother with anything else this just makes sure that the value exists and is not to set at none 
    print('valid')
else:
    print('invalid')

#this can create the confusion that we are saying that we need username and . in domain name but the proper syntax for that would actually be if username in domain name and . in username these are 2 separate boolean expressions 
#there still need to be a domain name, so we need to have a boolean expressions which is quite hard 