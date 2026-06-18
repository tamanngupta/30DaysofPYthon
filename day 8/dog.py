dog = {
    'name' : 'pogo',
    'breed': 'pug',
    'age' : 7
}
student = {
    'fnn':'Tamanna',
    'ln':'Gupta',
    "ag": 18,
    'marital_status':'unmarried',
    'country':'India',
    'city':'Delhi ',
    'skill':'unemployed'
}

print(len(student))

print(student['skill'])
print(type(student['skill']))

student['skill'] = 'python'
print(student)

print(student.keys())
print(student.values())
print(student.items())

del student['skill']
print(student)

del dog