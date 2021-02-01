'''import re

text = 'annahari.ram97@gmail.com rajujyothi.ram97@gmail.com'

pattern = re.compile('[a-zA-Z0-9]+\.+[a-z0-9]+@[a-z]+\.+[a-z]+')

result = pattern.findall(text)

print(result)'''

import datetime

today = datetime.date.today()
print(today)
birthday = datetime.date(2001, 2, 6)
print(birthday)
days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today + tdelta)

print(today.day)
print(today.weekday())
