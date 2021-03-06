from celery import Celery

app = Celery(
    "proj",
    broker="pyamqp://ricepotato:1234@localhost:5672/ricepotato",
    backend="rpc://",
    include=["proj.tasks"],
)

app.conf.timezone = "Asia/Seoul"
app.conf.update(result_expires=3600)
app.conf.beat_schedule = {
    "add-every-5-seconds": {"task": "proj.tasks.sleep", "schedule": 10, "args": (3,)}
}
