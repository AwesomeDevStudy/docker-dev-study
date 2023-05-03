## 실습 3-1. SQL 테스트를 위한 MySQL 5.7

```bash
# mysql 5.7 다운로드
docker pull mysql:5.7
```

<img src="assets/image-20230502232451373.png" alt="image-20230502232451373" style="zoom:50%;" />

- M1 MacOS의 경우 에러가 발생하므로 --platform을 지정해야됨

<img src="assets/image-20230502232848727.png" alt="image-20230502232848727" style="zoom:50%;" />

- docker pull을 할 때도 똑같이 플랫폼 지정 필요
- 결국 mysql:5.7 version은 실패하고, mysql:8.0.33 버전으로 진행
  - /etc/init.d/mysql 파일이 존재하지 않음

![image-20230503233359312](assets/image-20230503233359312.png)

## 실습 3-2. cAdvisor 컨테이너 실행

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

![image-20230503234412789](assets/image-20230503234412789.png)

- M1의 경우 실습에 나온 google/cadvisor로 돌리면 오류가 발생 -> zcube/cadvisor로 변경
- 도커가 설치된 호스트의 IP는 기본 localhost를 사용하니까 제대로 구동 되는 것을 확인

![image-20230503234819050](assets/image-20230503234819050.png)

![image-20230503235133383](assets/image-20230503235133383.png)

- CPU 실시간 동작도 확인 가능 (유용하게 사용 가능할듯)
