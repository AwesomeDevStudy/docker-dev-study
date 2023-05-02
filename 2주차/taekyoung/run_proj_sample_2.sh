#! /bin/bash

echo "@create docker container"

docker run -d --rm -it --net nginx-lb -v ./proj_sample/play.js:/play.js:ro --name=node_test_1 node node /play.js
docker run -d --rm -it --net nginx-lb -v ./proj_sample/play.js:/play.js:ro --name=node_test_2 node node /play.js
docker run -d --rm -it --net nginx-lb -v ./proj_sample/play.js:/play.js:ro --name=node_test_3 node node /play.js

docker run -d --rm -it --net nginx-lb -p 8000:8000 -v ./nginx_lb.conf:/etc/nginx/conf.d/nginx_lb.conf:ro --name=nginx_1 nginx

echo "@sleep 5sec"
sleep 5s
echo "@send curl test"

curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000

echo "@kill container wait..."
docker stop node_test_1
docker stop node_test_2
docker stop node_test_3
docker stop nginx_1

