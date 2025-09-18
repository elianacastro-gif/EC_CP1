#EC 1st Booleans notes

import time 
import datetime as date

current_time = time.time()
readable_time = time.ctime(current_time)
new_current_time = date.datetime.now()
hour = new_current_time.strftime("%h")
#minutes = %M
#weekday = %A, %a
#day = %d
#month = %B. %b
#month num = %m
#year = %Y, %y
#seconds = %S
over = True 



print(f"current time in seconds since january 1, 1970(epoch): {current_time}")
print(f"current time from datetime : {new_current_time}")
print(f"today is {readable_time}")
print(f"the hour is: {hour*3}")

print(f"the hour is saved as an integer: {isinstance(hour, int)}")
print(f"the hour is saved as an float: {isinstance(hour, float)}")
print(f"the hour is saved as an string: {isinstance(hour, str)}")

print(f"has a value: {bool(True)}")