from apscheduler.schedulers.blocking import BlockingScheduler
from flask_api.datascraper.main import update, lastupdate

sched = BlockingScheduler(timezone='Europe/Warsaw')

# The clock sends to API a request, which start an update.
# checks if up to date
@sched.scheduled_job('interval', minutes=120, id='interval_check')
def timed_job():
    print('Sending request for update - every 2h.')
    count = 0
    last = update()
    while last != 0 or count != last:
        count = last
        print(f"Still missing {last} records of Lottery.")
        last = update()
    print("None records missing, the datebase is up to date.")


# gets the newest scores
@sched.scheduled_job('cron', day_of_week='1,3,5', hour=22, minute=10, id='lottery_check')
def scheduled_job():
    print('Sending request for newest scores at 22:10')
    lastupdate()

sched.start() 