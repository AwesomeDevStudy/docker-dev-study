# 3주차 Dockerfile 실습내용

```bash
# docker_as_infra_trial
$ docker build -t sampleapi:3.0 .
$ docker run --rm -d -p 8080:8000 sampleapi:3.0
$ curl localhost:8080/test/page/
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    this is new test page.
</body>
</html>
```

```bash
# healthcheck_trial
$ docker build -t nothealthy:3.0 .
$ docker run --name submarine --rm -d -p 8080:8000 nothealthy:3.0

$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS                    PORTS                    NAMES
7bf10cc2dbe7   nothealthy:3.0   "uvicorn app.main:ap…"   52 seconds ago   Up 51 seconds (healthy)   0.0.0.0:8080->8000/tcp   submarine
```