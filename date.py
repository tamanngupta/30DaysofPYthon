from datetime import datetime

now = datetime.now()
print(now)
print(now.month)
print(now.timestamp)


new_year = datetime(2027, 1, 1)
print(new_year)
print(new_year.month)

t = now.strftime