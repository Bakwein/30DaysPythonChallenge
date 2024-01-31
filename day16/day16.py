from datetime import datetime
t = datetime.now()
print(t)
year = t.year
month = t.month
day = t.day
hour = t.hour
minute = t.minute
second = t.second
timestamp = t.timestamp()
print(hour,".",minute,".",second,sep="")
print(day,"/",month,"/",year,sep="")
print(timestamp)

print()

now = datetime.now()
t = now.strftime( "%m/%d/%Y, %H:%M:%S")
print(t) #2/01/2024, 02:25:37

date = "5 December, 2019"
data = datetime.strptime(date, "%d %B, %Y")
print(data)

from datetime import date

now = date(year=2024,month=2,day=1)
next_year = date(year=2025,month=1,day=1)
print(next_year-now) #335 days, 0:00:00

prev = date(year=1970,month=1,day=1)
print(now-prev) #19754 days, 0:00:00
