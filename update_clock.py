from apscheduler.schedulers.blocking import BlockingScheduler
from flask_api.updater.main import update_last, update_queue

sched = BlockingScheduler(timezone='Europe/Warsaw')

# The clock sends to API a request, which start an update.
# checks if up to date
@sched.scheduled_job('interval', minutes=60, id='interval_check')
def timed_job():
    print('Sending request for update - every 1h.')
    update_queue()


# gets the newest scores
@sched.scheduled_job('cron', hour=22, minute=10, id='lottery_check')
def scheduled_job():
    print('Sending request for newest scores at 22:10')
    update_last()

print("Starting initial update.")
update_queue()

sched.start() 