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

