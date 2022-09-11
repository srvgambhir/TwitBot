from apscheduler.schedulers.blocking import BlockingScheduler
import main

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=1)
def scheduled_job():
    print('This job is run everyday at midnight.')
    main.tweet()


