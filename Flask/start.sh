#!/bin/bash
app="iframe-flask-dashboard"
docker build -t ${app} .
docker run -dit -p 56733:80 \
  --name=${app} \
  -v $PWD/app ${app}
