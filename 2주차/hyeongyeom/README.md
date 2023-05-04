# 도커 스터디

# 실습

## 3-1 MySQL 컨테이너 실행

```bash
$ docker pull --platform linux/amd64 mysql:5.7 
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5c542010-23ee-4cc8-9ca6-e5ae9e2948f9/Untitled.png)

```bash
$ docker run --platform linux/amd64 -d -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=root --name mysql _container mysql:5.7
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f62c606-7918-4aab-b8af-9b8fc1b7b4ec/Untitled.png)

## 3-2 컨테이너 모니터링 도구 cAdviosr 컨테이너 실행

```bash
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=9559:8080 \
  --detach=true \
  --name=cadvisor \
  zcube/cadvisor:latest
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1b3557cf-26d1-47ba-81f5-4ab42a315806/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8898f99-dfff-4014-b876-06d3be907574/Untitled.png)

## 3-3 Nginx 컨테이너 실행

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2a9dfcc5-b7c9-4926-baa2-5a0723349308/Untitled.png)

### nginx index.html 파일 수정(copy 방식)

 

```bash
docker cp index.html webserver1:/usr/share/nginx/html/index.html
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fec3814a-8117-498f-a0b4-2a6550571028/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c32c682-cebc-4be3-b294-565ed6285930/Untitled.png)

## 3-6 도커 볼륨 활용

- 마운트

```bash
docker run -d --name vol-test1 \
> --mount source=my-appvol-1,target=/app \
> ubuntu:20.04
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f522f68-62d8-423b-a2bd-51dc0c3bfe02/Untitled.png)

- 볼륨

```bash
docker run -d --name vol-test2 \
> -v my-appvol-1:/var/log \
> ubuntu:20.04
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b73a1796-f101-4ae9-8f2f-597df5ed18ba/Untitled.png)

바인드 마운트 vs 볼륨 

- 볼륨은 도커 영역안에서 관리된다.
- 바인드 마운트의 경우 외부(host)에서 컨테이너 안쪽으로 내용을 추가할 수 있지만 볼륨은 그렇지 않다.