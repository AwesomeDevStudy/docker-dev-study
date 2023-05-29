# 5주차 실습: MicroK8s 실습

## 실습 컴퓨팅 환경

### Service node

1. rasberry pi:
    Mem: 3.7Gi, CPU: x4, OS: Ubuntu 22.04.2 LTS

### Worker node

1. oracle cloud instance(free-tier):
    Mem: 964Mi, CPU: x2, OS: Ubuntu 22.04.2 LTS
2. oracle cloud instance(free-tier):
    Mem: 964Mi, CPU: x2, OS: Ubuntu 22.04.2 LTS
3. google cloud instance(free-tier):
    Mem: 966Mi, CPU: x2, OS: Ubuntu 20.04.5 LTS

## 환경 설정

### MicroK8s 설치

1. snap 명령어를 사용한 microk8s 설치 및 권한 인가
```bash
$ sudo snap install microk8s --classic --channel=1.27
$ sudo usermod -a -G microk8s $USER
$ sudo chown -f -R $USER ~/.kube
$ microk8s kubectl get nodes
```
2. microk8s의 Dashboard, DNS 기능 활성화
```bash
$ microk8s enable dns
$ microk8s enable dashboard
```
