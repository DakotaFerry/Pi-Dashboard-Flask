#!/bin/bash
app="flaskboard"

docker build -t ${app} .
docker run -d -network="host"-p 5000:80 \
  --name=${app} \
  -v $PWD:/app ${app}

firefox localhost:5000
