import json

person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"] }


person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dctt = json.dumps(person_dct)
print(person_dctt)

p = json.loads(person_json)
print(p)

def readd(filepath):
    f = open(filepath)
    