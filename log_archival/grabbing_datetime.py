from datetime import date
from datetime import datetime

today = date.today()
print(today)

now = datetime.now()
print(now)

format = now.strftime("%m/%d/%y,%H:%M:%S")
print(format)
