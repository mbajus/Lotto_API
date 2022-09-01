from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(timezone="Europe/Warsaw")

@sched.scheduled_job("interval", minutes = 1.5)
def timed_job():
    print("XD mineło mało czasu")

@sched.scheduled_job("cron", hour=14, minute=36)
def scheduled_job():
    print("XD WUDZIESTA")

sched.start()