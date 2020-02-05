from crontab import CronTab
#init cron
cron   = CronTab()
cmd = 'python /Users/yunheekang/pet_ftp/test_ftp_petbox.py'
#add new cron job
job  = cron.new(command=cmd)

#job settings
job.hour.every(4)
