#import calendar

#print(calendar.weekday(2021, 2, 14))

# print(calendar.isleap(2020))
# print(calendar.isleap(2018))
#
# print(calendar.leapdays(2000, 2021))
# print(calendar.isleap(2001))

#import time

# start = time.time()  # Prints UNIX time - seconds from 01/01/1970
# #time2 = datetime.datetime(2002, 7, 12)
# #time2 = datetime.
# time.sleep(2)  # adds delay
# end = time.time()  # difference
# print(end - start)  # difference between end / start
#
# print(time.asctime())
# print(time.gmtime())
# date_now = time.gmtime()
# print(date_now[0], date_now[1], date_now[])
# import datetime
#
# d = datetime.date(2018, 7, 22)
# today = datetime.date.today()
# print(today)
# print(type(d))
# print(d)
# print(type(today))
# d = datetime.date(2000, 6, 15)
# today = datetime.date.today()
# print(today - d)
# difference = today - d
#
#
# print(today.year)
# print(today.month)
# print(today.day)
#
# print(today.year, today.month, today.day)

import datetime

today = datetime.date.today()

print(today.weekday())  # Monday 0 Sunday 6
print(today.isoweekday())  # Monday 1 Sunday 7

today = datetime.date.today()
delta = datetime.timedelta(days=7)
print(today + delta)

today = datetime.date.today()
bday = datetime.date(2021, 3, 17)
till_bday = bday - today
print(till_bday)

t = datetime.time(13, 24, 10)
print(t)  # Will print time with all parameters
print(t.hour)  # will print only hours

# dt = datetime.datetime(2020, 11, 30, 18, 20, 36, 100000)
# print(dt)
# print(dt.date().year)  # Will print date only
# print(dt.time())  # Will print time only
# print(str(dt.date()))

# dt = datetime.datetime(2020, 11, 30, 18, 20, 36, 100000)
# dt_delta = datetime.timedelta(days=7, hours=15, milliseconds=10)
# print(dt + dt_delta)  # Will print datetime after timedelta

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# print(dt_today)
# print(dt_now)

dt_today = datetime.datetime.today()
print(dt_today.strftime("%B %d, %Y"))   # Will print formatted date where %B is full month, %d day as number,
                                        # %Y full year with century as decimal number in YYYY format.

dt_str = "November 30, 2020"
str_to_date = datetime.datetime.strptime(dt_str, '%B %d, %Y') # Converts string into datetime fromat
print(str_to_date)
print(type(str_to_date))