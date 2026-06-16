tpl = tuple()
b = ('aryan', 'rohit')
s = ('pooja', 'avoo')
siblings = b + s
print(siblings)
num = len(siblings)
print(f"I have {num} siblings")
parents = ('kusum', 'raj')
family = parents + siblings
print(family)
sib = family[2:]
par = family[0:2]
print(sib, par)
