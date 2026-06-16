# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('twitter')
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)

print(A.union(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

m = len(age)
st = set(age)
t = len(st)
print(m>t)

# 1. The exact sentence from the exercise
sentence = "I am a teacher and I love to inspire and teach people."

# 2. REMOVE the period first, then SPLIT into words
# This creates a list: ['I', 'am', 'a', 'teacher', ...]
words_list = sentence.replace(".", "").split()

# 3. Convert the LIST of words into a set
# This removes duplicates like 'I' and 'and'
unique_words_set = set(words_list)

# 4. Count the items in the set
result = len(unique_words_set)

print("Your unique words are:", unique_words_set)
print("The count is:", result)

j = 'tf just happened.'
words_lis = j.replace('.','').split()
un = set(words_lis)
print(un)