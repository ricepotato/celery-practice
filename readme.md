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

```bash
  celery --broker=amqp://ricepotato:1234@localhost:5672/ricepotato flower --broder_api=http://ricepotato:1234@localhost:15672/api/
```

## rabbitmq

실행

```bash
  docker-compose up
```

conf, logs, home 읽기/쓰기 권한 필요

최초 실행 후 계정 설정, vhost 생성 권한설정 필요. 😅

### ports

- 15672 : 관리자 web UI
- 5672 : 서비스 포트

### 계정 설정 / 권한 설정

username 계정 설정


```bash
  rabbitmqctl add_user {username} {password}
```

administrator 권한 설정

```bash
  rabbitmqctl set_user_tags {username} administrator
```

vhost 생성 / 권한 설정

```bash
  rabbitmqctl add_vhost {vhost_name}
```

```bash
  rabbitmqctl set_permission -p {vhost_name} ".*" ".*" ".*"
```

