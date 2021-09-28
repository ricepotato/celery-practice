import time
from .celery import app

LOCK_EXPIRE = 60 * 10  # Lock expires in 10 minutes


@app.task
def add(x: int, y: int) -> int:
    return x + y


@app.task
def mul(x: int, y: int) -> int:
    return x * y


@app.task
def xsum(numbers: list) -> int:
    return sum(numbers)


@app.task
def sleep(sec: int) -> bool:
    print("sleep start...")
    time.sleep(sec)
    print("sleep end...")
    return True


@app.task
def divide_by_zero():
    return 3 / 0


@app.task
def div(a: int, b: int) -> float:
    return a / b
