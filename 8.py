import time
from datetime import datetime, date

try:
    day, month, year = raw_input("Enter DOB formated day/month/year: ").split("/")
except ValueError:
    print("Invalid date")

try:
    DOB = datetime(int(year), int(month), int(day))
except ValueError:
    print("Invalid date")

now = datetime.now()

delta = now - DOB

if delta.days < 18*365:
    print("You are under 18")
