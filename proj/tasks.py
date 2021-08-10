import time
from .celery import app

LOCK_EXPIRE = 60 * 10  # Lock expires in 10 minutes


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def sleep(sec):
    print("sleep start...")
    time.sleep(sec)
    print("sleep end...")
    return True
