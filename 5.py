import time
from datetime import datetime, date

try:
    day, month, year = raw_input("Enter DOB formated day/month/year").split("/")
except ValueError:
    print("Invalid date")

try:
    DOB = datetime(int(year), int(month), int(day))
except ValueError:
    print("Invalid date")

now = datetime.now()

delta = now - DOB

print("You have been alive for {} days and {} seconds!".format(
    delta.days,
    delta.days * delta.seconds))
