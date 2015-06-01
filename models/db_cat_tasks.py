from gluon.scheduler import Scheduler

myscheduler = Scheduler(db)

def count_cats():
    return db(db.cat).count()
