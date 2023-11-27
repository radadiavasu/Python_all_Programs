from datetime import datetime, timezone, timedelta

# print(datetime.now())

# print(datetime.now(timezone.utc)) # Universal Time Coordinated

today = (datetime.now(timezone.utc))
tommorow = today + timedelta(days=1)

print(today)
print(tommorow)

print(today.strftime('%d-%m-%Y %H:%M:%S')) # String format time

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')

print(user_date)