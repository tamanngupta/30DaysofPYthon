from datetime import datetime, date

now = datetime.now()
print(now)
print(now.month)
print(now.timestamp)


new_year = datetime(2027, 1, 1)
print(new_year)
print(new_year.month)

t = now.strftime("%d/%m/%Y")
print(t)

d= date(2020, 1, 1)
print(f'current date is {d.today()}')

date_string = "1 January, 1970"
m = datetime.strptime(date_string, "%d %B, %Y")
print(m)

t3 = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
n = now - t3
print(n)