from datetime import datetime
now = datetime.now()
print(now) #2024-02-01 02:06:38.449879
day = now.day
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)# 1 2 2024 2 6
print('timestamp', timestamp) # timestamp 1706742398.449879
print(f'{day}/{month}/{year}, {hour}:{minute}') #1/2/2024, 2:6

#Formatting Date Output Using strftime
new_year = datetime(2020, 1, 1) #daha fazla da daha az da parametre verilebilir
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

#https://strftime.org

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
'''
time: 02:09:19
time one: 02/01/2024, 02:09:19
time two: 01/02/2024, 02:09:19
'''

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

'''
date_string = 5 December, 2019
date_object = 2019-12-05 00:00:00
'''

#Using date from datetime
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2024-02-01
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2024
print("Current month:", today.month) # 2
print("Current day:", today.day)     # 1

#Time Objects to Represent Time

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

'''
a = 00:00:00
b = 10:30:50
c = 10:30:50
d = 10:30:50.200555
'''

#Difference Between Two Points in Time Using
today = date(year = 2024, month=2,day=1)
print(today)
prev_year = date(year=2020, month=1, day=1)
time_left_for_newyear = prev_year - today
print(time_left_for_newyear)

print()

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00