# celery practice

## run

worker 시작 한번에 하나의 task 만 실행

```bash
  celery -A proj worker --concurrency=1
```


celery beat 실행

```bash
  celery -A proj beat -s ./celerybeat-schedule
```

celery flower 실행

```bash
  celery -A proj flower
```
