# 도커 스터디

# 실습

## 3-1 MySQL 컨테이너 실행

```bash
$ docker pull --platform linux/amd64 mysql:5.7 
```

![practice-image1](assets/practice-image1.png)

```bash
$ docker run --platform linux/amd64 -d -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=root --name mysql _container mysql:5.7
```

![practice-image2](assets/practice-image2.png)


![practice-image3](assets/practice-image3.png)
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

![practice-image4](assets/practice-image4.png)

![practice-image5](assets/practice-image5.png)

![practice-image6](assets/practice-image6.png)

## 3-3 Nginx 컨테이너 실행

![practice-image7](assets/practice-image7.png)

### nginx index.html 파일 수정(copy 방식)

 

```bash
docker cp index.html webserver1:/usr/share/nginx/html/index.html
```

![practice-image8](assets/practice-image8.png)



## 3-6 도커 볼륨 활용

- 마운트

```bash
docker run -d --name vol-test1 \
> --mount source=my-appvol-1,target=/app \
> ubuntu:20.04
```


- 볼륨

```bash
docker run -d --name vol-test2 \
> -v my-appvol-1:/var/log \
> ubuntu:20.04
```

![practice-image9](assets/practice-image9.png)

바인드 마운트 vs 볼륨 

- 볼륨은 도커 영역안에서 관리된다.
- 바인드 마운트의 경우 외부(host)에서 컨테이너 안쪽으로 내용을 추가할 수 있지만 볼륨은 그렇지 않다.