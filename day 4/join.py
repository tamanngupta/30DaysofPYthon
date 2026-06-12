bruh = ['thirthy', 'days', 'of', 'pyhton']
pri = ' '.join(bruh)
print(pri)

brin = ['coding', 'for', 'all']
prit = ' '.join(brin)
print(prit)

company = "coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip('coding'))
print(company.find('coding'))
print(company.replace('coding','python'))
shit = 'python for all'
print(shit.replace('all','everyone'))
print(shit.split())
bro = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(bro.split(','))

first_c = company[0]
print(first_c)

print(company.index('c'))
print(company.index('f'))
print(company.rindex('i'))
him = 'You cannot end a sentence with because because because is a conjunction'
print(him.rindex('because'))
print(him.strip('because because because'))

start = int(him.find('because because because'))
end = start + len(him)
slic = him[start:end]
print(slic)

print(him.replace('because because because', ''))

print(him.index('because'))

print(company.startswith('coding'))
print(company.endswith('coding'))

cross = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
listi = '# '.join(cross)
print(listi)
print('I am enjoying this challenge\nI just wonder what is next')
print('name\tage\tcountry\tcity\ntamanna\t18\tindia\tdelhi')