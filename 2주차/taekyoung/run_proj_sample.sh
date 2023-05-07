#! /bin/bash

echo "@create docker container"

docker run -d --rm -it -p 127.0.0.1:8002:8002 -v ./proj_sample/play.js:/play.js:ro --name=node_test node node /play.js

echo "@bind moundted volume"
docker inspect --format="{{ .HostConfig.Binds }}" node_test

echo "@sleep 3sec"
sleep 3s
echo "@send curl test"
curl localhost:8002
echo "@kill container wait..."
docker stop node_test

