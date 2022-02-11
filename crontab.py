
import datetime as dt
from scheduler import Scheduler
import scheduler.trigger as trigger

def foo():
    print("Sukses..")

schedule = Scheduler()
schedule.minutely(dt.time(second=15), foo)   

while True:  
    schedule.exec_jobs()
    time.sleep(1)