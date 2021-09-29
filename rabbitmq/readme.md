# rabbitmq docker

## 실행

```bash
  docker-compose up
```

conf, logs, home 읽기/쓰기 권한 필요

최초 실행 후 계정 설정, vhost 생성 권한설정 필요. 😅

## ports

- 15672 : 관리자 web UI
- 5672 : 서비스 포트

## 계정 설정 / 권한 설정

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

