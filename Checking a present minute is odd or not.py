#Checking the present minute is odd or even in your pc

from _datetime import datetime
import time
import random

odds=list(range(1,60,2))

for i in range(5):
    present_minute=datetime.today().minute

    if present_minute in odds:
        print('Present minute is odd!')
    else:
        print('Present minute is even!')
    work_time=random.randint(1,60)
    time.sleep(work_time)
