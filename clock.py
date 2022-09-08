from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler(timezone='Europe/Warsaw')

# The clock sends to API a request, which start an update.
# checks if up to date
@sched.scheduled_job('interval', minutes=15, id='interval_check')
def timed_job():
    print('Sending request for update - every 2h.')
    req = requests.get('https://api-lotto.herokuapp.com/update')
    print(req)

# gets the newest scores
@sched.scheduled_job('cron', day_of_week='1,3,5', hour=22, minute=10, id='lottery_check')
def scheduled_job():
    print('Sending request for newest scores at 22:10')
    req = requests.get('https://api-lotto.herokuapp.com/lastupdate')
    print(req)

sched.start() 