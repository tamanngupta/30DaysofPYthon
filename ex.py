import re
import requests
import collections
import statistics

url = 'https://substack.com/@pythonclcoding/note/c-296955465?utmSource=%2Fsearch%2Fpython'

responses = requests.get(url)

if responses.status_code == 200:
    text = responses.text

    tl = text.lower()

words = re.findall(r"\b\w+\b", tl)

words_counts = collections.Counter(words)

most_common = words_counts.most_common(10)
print(most_common)


urlll = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(urlll)

if response.status_code == 200:
    txt = response.text

weights = re.findall('weight')

meaan = stastictics.mean(weights)
print(meaan)