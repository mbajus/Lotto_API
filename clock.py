from apscheduler.schedulers.blocking import BlockingScheduler
from flask_api.datascraper.main import check_db

sched = BlockingScheduler(timezone='Europe/Warsaw')

# initial check up with updating
@sched.scheduled_job('interval', minutes=5, id='initial_check')
def initial_check():
    print('Checking DB, if update needed...')
    check_db()


# checks if up to date
@sched.scheduled_job('interval', hours=6, id='interval_check')
def timed_job():
    print('Webscraper is chcecking for updates - every 2h checks.')

# gets the newest scores
@sched.scheduled_job('cron', day_of_week='1,3,5', hour=22, minute=10, id='lottery_check')
def scheduled_job():
    print('Webscraping after lottery - 22h10')

sched.start()