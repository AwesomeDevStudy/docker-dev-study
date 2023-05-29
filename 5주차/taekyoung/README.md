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






minikube를 사용해 로컬 환경에서 연습해 보기.
원래는 kubeadm을 오라클 클라우드 혹은 구글 클라우드의 무료 컴퓨팅 인스턴스에 설치하고 테스트를 진행해 보고 싶었으나, 무료 버전의 제한된 컴퓨팅 사양으로 인해 로컬 환경(WSL Ubuntu 20.04.4 LTS)에서 테스트를 진행하기로 한다.
만약 RasberryPI가 있다면 거기서 실행해 보는 것도 좋은 생각일 것이다.

미니쿠베를 활용하기 위해서는 아래와 같은 최소 환경이 갖춰줘야 한다.

2 CPUs or more
2GB of free memory
20GB of free disk space
Internet connection
Container or virtual machine manager, such as: Docker, QEMU, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMware Fusion/Workstation
여기서 눈여겨볼 점은 마지막 조건인데 컨테이너 혹은 가상환경으로 도커뿐만 아니라 다른 환경들도 사용 가능하다는 것이다.

minikube 설치
minikube 공식 도큐멘트

위 링크에서 환경에 맞는 미니쿠베를 다운로드할 수 있다



리눅스, x86-64 아키텍쳐 환경에 최신버젼의 미니쿠베를 다운로드하는 명령어이다.

💡 $ uname -a # 명령어로 리눅스 환경의 아키텍쳐를 확인할 수 있다.
위에서 제공하는 명령어를 사용해 다운로드를 실행해보자
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
미니쿠베를 실행하면 자동으로 설치된 도커 드라이버를 탐지하고, 미니쿠베 컨트롤 플레인 구성에 필요한 베이스 이미지들을 다운로드받는다
minikube start
#😄  minikube v1.29.0 on Ubuntu 20.04
#✨  Using the docker driver based on existing profile
#👍  Starting control plane node minikube in cluster minikube
#🚜  Pulling base image ...
#🏃  Updating the running docker "minikube" container ...
#🐳  Preparing Kubernetes v1.26.1 on Docker 20.10.23 ...
#🔎  Verifying Kubernetes components...
#    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
#🌟  Enabled addons: storage-provisioner, default-storageclass
#🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
위 명령어를 통해서 kubectl도 함께 설치가 되고, 설치된 kubectl은 minikube를 사용하도록 설정된다. 아래의 명령어를 통해 minikube가 실행중인 클러스터를 확인 가능하다
kubectl get po -A
#NAMESPACE     NAME                               READY   STATUS    RESTARTS       AGE
#kube-system   coredns-787d4945fb-66dpd           1/1     Running   1 (2m1s ago)   3m6s
#kube-system   etcd-minikube                      1/1     Running   2 (2m1s ago)   3m21s
#kube-system   kube-apiserver-minikube            1/1     Running   1 (2m1s ago)   3m20s
#kube-system   kube-controller-manager-minikube   1/1     Running   2 (2m1s ago)   3m20s
#kube-system   kube-proxy-fkpkw                   1/1     Running   2 (2m1s ago)   3m7s
#kube-system   kube-scheduler-minikube            1/1     Running   1 (2m6s ago)   3m20s
#kube-system   storage-provisioner                1/1     Running   2 (101s ago)   3m18s
아래의 명령어를 실행하면 워커노드로 실행중인 컨테이너화된 애플리케이션들의 목록을 브라우저에서 확인할 수 있다. (아직 실행한 애플리케이션이 없으므로 표시하는 데이터가 없을것이.)
minikube dashboard
실행중인 미니쿠베를 정지하고, 클러스터를 제거하자
minikube stop

minikube delete --all
minikube로 멀티노드 클러스터 실행
1개의 컨트롤 플레인과 3개의 워커 노드를 가지는 쿠버네티스 클러스터를 생성하자
minikube start --nodes 4 -p multinode-demo
# multinode-demo, multinode-demo-m02, multinode-demo-m03 등의 이름을 갖는 노드들을 생성할 것이다.
생성된 노드들의 상태를 확인할 수 있다
kubectl get nodes
노드에 대한 자세한 정보를 확인해 보자
kubectl describe node multinode-demo
클러스터에 첫 애플리케이션 실행
블로그의 Kubernetes를 위한 도커 사용을 따라했다면 기존에 도커허브에 푸쉬했던 이미지를 떠올릴 수 있을것이다

kubectl run 명령어를 사용해 간단한게 푸쉬했던 이미지를 실행해보자
kubectl run kubia --image=<docker_id>/kubia --port=8080
# kubectl run kubia --image=ltyiz07/kubia --port=8080 --generator=run/v1
# 위에서 --getnerator=run/v1 옵션은 v1.18 버젼부터 지원하지 않는다
# 만약 파드를 생성하는 과정에서 실수를 했다면 
# kubectl delete pod kubia # 명령어로 파드를 제거할 수 있다
생성된 파드를 조회하고 상태를 확인해보자 (시간이 지남에 따라 Status 가 Pendding 에서 Running 으로 변경될 것이다)
파드 내부에는 하나 혹은 그 이상의 컨테이너들이 실행 될 수 있는데, 각 파드는 자체 IP, 호스트 이름, 프로세스 등이 있는 논리적으로 분리된 머신이다

파드내부에서 실행중인 컨테이너는 논리적으로 분리된 머신임으로 호스트의 도커 컨테이너 리스트에 뜨지 않는다

kubectl get pods
지금까지 백그라운드에서 일어난 동작들을 이해해보자.
kubectl을 통해서 도커허브에 푸쉬된 이미지를 실행시켰다.



kubectl 명령어를 실행하면 쿠버네티스의 API 서버로 REST HTTP 요청을 전달하고
클러스터에 새로운 레플리카 셋을 오브젝트를 생성한다
레플리카 셋은 새로운 파드를 생성하고 스케줄러에의해 워커 노드 중 하나에 스케줄링된다
해당 워커 노드의 Kubelet은 파드가 스케줄링됐다는 것을 보고 이미지가 로컬에 없지 때문에 도커에게 특정 이미지를 풀 하도록 지시한다
이미지를 다운로드하고 도커는 컨테이너를 생성하고 실행한다
웹 애플리케이션에 접근하기
실행중인 파드에 어떻게 접근할 수 있을까? 각 파드는 자체 IP 주소를 가지고 있지만 이 주소는 클러스터 내부에 있으며 외부에서는 접근이 불가능하다. 외부에서 파드에 접근을 가능하게 하려면 서비스 오브젝트를 통해 노출해야 한다. 파드와 마찬가지로 일반적인 서비스(Cluster IP 서비스)를 생성하면 이것은 클러스터 내부에서만 접근 가능하기 때문에 LoadBalancer 유형의 특별한 서비스를 생성해야한다. LoadBalancer 유형의 서비스는 외부 로드 밸런서에 생성되므로 로드 밸런서의 IP를 통해 파드에 연결할 수 있다.

서비스 오브젝트 생성하기
서비스를 생성하기 위해 쿠버네티스에게 앞서 생성한 레플리카 셋을 노출하도록 명령하고, 생성된 서비스를 조회해보자
원래대로면 얼마간 후에 EXTERNAL-IP 가 Pending 에서 접속 가능한 IP 로 바뀌어야 하지만 minikube는 로드밸런서를 지원하지 않아서 계속 Pending 상태에 있게 된다.

kubectl expose po kubia --type=LoadBalancer --name kubia-http

kubectl get services
#minikube가 아닌 gke나 kubeadm을 사용중이라면 EXTERNAL-IP에 접속 가능한 IP를 보여줄 것이다
minikube는 다른 방식으로 접근이 가능하다

#방법 1
# 실행시 자동으로 브라우저에 할당된 url로 접속될 것이다
minikube -p multinode-demo service kubia-http

#방법 2
# 해당 서비스에 연결된 url을 확인할 수 있고, 수동으로 접속 가능하다
minikube -p multinode-demo service kubia-http --url

#방법 3
# kubectl 의 port-forward 기능을 사용하는 방식이다, localhost:7080 으로 접속하면 된다
kubectl port-forward service/kubia-http 7080:8000
지금까지 컨테이너들을 직접 실행시키는 대신, 쿠버네티스의 기본 빌딩블록인 파드를 이용해 애플리케이션을 실행시켰다.

그러나 파드도 직접 실행시키지 않고, kubectl run 명령으로 레플리카 셋을 생성하고, 생성된 레플리카 셋이 실제 파드를 생성한다.

그리고 클러스터 외부에서 접근하기 위해 쿠버네티스에게 레플리카 셋에 의해 관리되는 모든 파드를 단일 단일 서비스로 노출하도록 명령한다.

