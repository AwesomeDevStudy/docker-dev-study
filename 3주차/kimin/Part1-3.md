## 실습 4-1. 쉘 스크립트를 이용한 환경 구성 실습

```bash
# Dockerfile 빌드
docker build -f Dockerfile.ex4_1 -t webapp:7.0 .
```

```bash
# 컨테이너 실행
docker run -itd -p 8007:80 --name webapp07 webapp:7.0
```


- 정상적으로 실행된 모습을 확인할 수 있음
- Dockerfile 빌드 시 echo에서 > 표시를 한번만 적으면 실행은 빌드는 되는데, 컨테이너 실행시 run이 안됨
- 이때는 docker log 명령어를 활용하여 컨테이너 로그를 확인해야됨

## 실습 4-2. ADD 명령어의 자동 압축 해제

```bash
# 깃허브에서 압축 파일 다운로드
git clone https://github.com/brayanlee/webapp.git
mv webapp/webapp.tar.gz  .
```

```bash
# Dockerfile 빌드
docker build -f Dockerfile.ex4_2 -t webapp:8.0 .
```

```bash
# 컨테이너 실행
docker run -itd -p 8008:80 --name webapp08 webapp:8.0
```

- 정상적으로 실행된 모습을 확인할 수 있음
- 많이 사용할 일이 있을까 싶다. 
- CMD가 아닌 ENTRYPOINT로 실행해도 동일한 결과를 얻음

## 실습 4-3. 이미지 용량 절감을 위한 실습

```bash
# Dockerfile 빌드
docker build -f Dockerfile.ex4_3 -t webapp:9.0 .
```

```bash
# 컨테이너 실행
docker run -itd -p 9000:80 --name webapp09 webapp:9.0
```

```bash
# 결과
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
webapp       9.0       1eea51526854   About a minute ago   204MB
webapp       8.0       58adf1f9c87a   33 minutes ago       266MB
```

- 기존에 비해 약 62MB가 줄어들었음을 확인할 수 있다.

### 다이브 실습
```bash
# 다이브 비교 1: 임시파일 유지
docker run --rm -it \
-v /var/run/docker.sock:/var/run/docker.sock \
-v "$(pwd)":"$(pwd)" \
-w "$(pwd)" \
-v "$HOME/.dive.yaml":"$HOME/.dive.yaml" \
wagoodman/dive:latest build -f Dockerfile.ex4_2  -t lab2-webapp:8.0 .
```

```bash
# 다이브 비교 2: 임시파일 삭제
docker run --rm -it \
-v /var/run/docker.sock:/var/run/docker.sock \
-v "$(pwd)":"$(pwd)" \
-w "$(pwd)" \
-v "$HOME/.dive.yaml":"$HOME/.dive.yaml" \
wagoodman/dive:latest build -f Dockerfile.ex4_3  -t lab2-webapp:9.0 .
```

