import datetime, bday_messages

from bday_messages import random_messages

today = datetime.date.today()
next_birthday = datetime.date(2026,6,1)
days_away = next_birthday - today
if today == next_birthday:
    print(random_messages) # （从 bday_messages 导入的）
else:
    print(f'My next birthday is {days_away} days away!')