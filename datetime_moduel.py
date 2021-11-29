from datetime import date

date_object = date(2018, 4, 21)
print(date_object)
print(type(date_object))



today = date.today()
print('Year:', today.year)
print('Month:', today.month)
print('Day:', today.day)

date_timestamp = date.fromtimestamp(1132895532)
print(date_timestamp)

from datetime import time

now = time()
print(now.microsecond)


from datetime import time

# default parameter values
time1 = time()
print("time1 =", time1)

# parameters and values
time2 = time(hour = 13, minute = 45, second = 56)
print("time2 =", time2)

# only values (order matters)
time3 = time(9, 25, 43)
print("time3 =", time3)

# hour, minute, second, microsecond
time4 = time(16, 3, 16, 128734)
print("time4 =", time4)

from datetime import time

t = time(14, 23, 45)

print("hour =", t.hour)
print("minute =", t.minute)
print("second =", t.second)
print("microsecond =", t.microsecond)


from datetime import datetime

dt1 = datetime(year=2012, month=3, day=22)
dt2 = datetime(2012, 3, 22, 11, 34, 16, 236744)

print(dt1)
print(dt2)

from datetime import datetime

current_date_time = datetime.now()
print(current_date_time)

from datetime import datetime

my_date = datetime.now()

# get ISO format
print('ISO format =', my_date.isoformat())

# get ISO weekday
print('ISO weekday =', my_date.isoweekday())

# get Year
print('Year =', my_date.year)

# get month
print('Month =', my_date.month)

# get day
print('Day =', my_date.day)



from datetime import datetime

my_date = datetime.now()

# convert datetime object to UNIX timestamp
timestamp = datetime.timestamp(my_date)
print('timestamp =', timestamp)

# convert UNIX timestamp to datetime object
dt = datetime.fromtimestamp(timestamp)
print('datetime =', dt)



from datetime import timedelta

td = timedelta(microseconds=3333)




from datetime import datetime, date

date1 = date(2020, 8, 13)
date2 = date(2019, 9, 14)
date3 = date2 - date1
print("date3", date3)

date4 = datetime(year = 2016, month = 5, day = 8, hour = 10, minute = 31, second = 44)
date5 = datetime(year = 2017, month = 4, day = 6, hour = 7, minute = 32, second = 12)
date6 = date5 - date4
print("date6 =", date6)

print("type of date3 =", type(date3))
print("type of date6 =", type(date6))



from datetime import timedelta

td1 = timedelta(weeks = 2, days = 7, hours = 12)
td2 = timedelta(days = 222, hours = 13, minutes = 45, seconds = 18)
td3 = td2 - td1

print("td3 =", td3)


from datetime import timedelta

td1 = timedelta(weeks = 2, days = 7, hours = 12)

print("Total seconds =", td1.total_seconds())


from datetime import datetime

string = "11 December, 2020"

dt = datetime.strptime(string, "%d %B, %Y")
print(dt)




from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)
