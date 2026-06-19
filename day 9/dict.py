person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

m = int( len(person['skills']) // 2 )
if 'skills' in person :
    print(person['skills'][m])


if 'skills' in person:
    print('Python' in person['skills'])

if 'Javascript' and 'React' in person['skills'] : 
    print('he is a frontend developer')
if 'Python' and 'Node' and 'MongoDB' in person['skills']:
    print('he is a backend developer')
if 'React' and 'Node' and 'MongoDB' in person['skills'] : 
    print('he is a fullstack developer')
else:
    print('unknown title')