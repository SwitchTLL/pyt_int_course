import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

from datetime import datetime

right_this_minute = datetime.today().minute

if (right_this_minute % 2 == 0):
    print("Current minute seems even.")
else:
    print("Current minute seems a little odd.")


# Original code

#from datetime import datetime
#import time
#import random

#odds = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31,
#33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59}

#right_this_minute = datetime.today().minute

#for i in range(5):
 #   if right_this_minute in odds:
  #      print("This is an odd minute")
   # else:
    #    print("Not an odd minute")