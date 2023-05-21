# 4주차 실습 내용

## docker compose 와 fastAPI 를 활용한 편리한 개발환경 세팅

### 이점
1. fastAPI를 사용한 개발시에 로컬 개발환경에 python 혹은 uvicorn 등의 종속성들의 설치가 필요 없이 개발을 시작할 수 있다.
2. Live-realoading을 지원해서 개발중인 파일을 변경하더라고 개발중인 서버를 수동으로 다시 시작하거나 할 필요가 없다.

### 실행 방법

```bash
$ cd trial_1
$ docker compose up -d
```
위 명령어를 사용하면 서버를 실행할 수 있습니다.
또한 "src" 디렉토리 내부의 소스코드를 수정하면 서버가 자동으로 재시작되어 개발에 편리합니다.

## docker compose 를 활용한 애플리케이션 스케일링

## 실습 방법

```bash
$ cd trial_2
$ docker compose up -d
$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS      NAMES
ee652f09bd61   redis:6-alpine   "docker-entrypoint.s…"   4 seconds ago   Up 2 seconds   6379/tcp   trial_2-server_db-1
ae812651b8fe   httpd:2          "httpd-foreground"       4 seconds ago   Up 2 seconds   80/tcp     trial_2-server_web-1
$ docker compose up --scale server_db=3 --scale server_web=3 -d
$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS      NAMES
4486f2ba5a0d   httpd:2          "httpd-foreground"       6 seconds ago   Up 4 seconds   80/tcp     trial_2-server_web-1
9eee9a3e0dbe   redis:6-alpine   "docker-entrypoint.s…"   7 seconds ago   Up 4 seconds   6379/tcp   trial_2-server_db-1
2246347cb8e9   redis:6-alpine   "docker-entrypoint.s…"   7 seconds ago   Up 4 seconds   6379/tcp   trial_2-server_db-2
d295b34b99f9   redis:6-alpine   "docker-entrypoint.s…"   7 seconds ago   Up 3 seconds   6379/tcp   trial_2-server_db-3
2a592d7d696b   httpd:2          "httpd-foreground"       7 seconds ago   Up 3 seconds   80/tcp     trial_2-server_web-3
2db2f3719277   httpd:2          "httpd-foreground"       7 seconds ago   Up 3 seconds   80/tcp     trial_2-server_web-2

$ docker compsoe down
```
scale 옵션을 사용하여 원하는 컨테이너의 개수를 명시해주면 해당 값만큼 2개의 컨테이너가 추가적으로 생성된 것을 확인할 수 있다.
또한 "docker compose down"을 실행하면 모든 컨테이너가 한번에 종료된다.


## docker compose 를 활용한 로드밸런싱

### 실습 방법
```bash
$ cd trial_3
$ docker compose up --build
```
실행 후에 browser 에서 [localhost:8080](http://localhost:8080) 접속
공들의 개수는 각각 서버의 휘발성 메로리에 저장되는데, 새로고침을 할 때마다 각각의 서버에 저당된 갯수를 보내주는 것을 확인할 수 있습니다.


