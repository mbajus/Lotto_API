from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone="Europe/Warsaw")

@sched.scheduled_job('interval', minutes=0.5)
def timed_job():
    print('This job is run every half minute.')

@sched.scheduled_job('cron', hour=14, minute=52)
def scheduled_job():
    print('This job is run every weekday at 14:50.')

sched.start()