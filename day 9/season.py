while True:
    s = input('enter month:')
    t = s.lower()
    autumn = ['september', 'octoebr', 'november']
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']
    winter = ['december', 'january', 'febraury']

    if t in autumn : 
        print('autumn is going on')
        break
    elif t in spring : 
        print('spring is going on')
        break
    elif t in summer : 
        print('summer is going on')
        break
    elif t in winter: 
        print('winter is going on')
        break
    else: 
        print('pls enter valid month')

