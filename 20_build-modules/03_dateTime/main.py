
# import datetime 

from datetime import datetime, timedelta

current_time = datetime.now()
print("Current time:", current_time)
print("Current time:", current_time.time())
print("Current time:", current_time.date())
print("Current Year:", current_time.year)
print("Current Month:", current_time.month)
print("Current Day:", current_time.day)


print("Current time:", current_time.strftime("%H:%M:%S"))
print("Current date:", current_time.strftime("%Y-%m-%d"))
print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
# print("Current date and time:", datetime.datetime.now())
# print("Current date:", datetime.date.today())


# future_date = current_time + timedelta(days=10)
future_date = current_time - timedelta(days=10)
print("Future date:", future_date)