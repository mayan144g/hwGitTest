import random
import datetime

currentYear = datetime.datetime.now().year
currentMonth = datetime.datetime.now().month

year = random.randint(0, currentYear)
month = random.randint(1, 12)

print(currentYear, '/', currentMonth)
print(year, '/', month)
print(currentYear - year, '/', currentMonth - month)