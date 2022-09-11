from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
import main

sched = BlockingScheduler(timezone=pytz.timezone('America/New_York'))

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def scheduled_job():
    print('This job is run everyday at noon.')
    main.tweet()

sched.start()
