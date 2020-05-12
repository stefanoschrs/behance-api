#!/bin/bash

port=15151
dockerName=behance-api
username=stefanoschrs
outFile=/tmp/${username}.behance.json
if [[ "$1" != "" ]]; then
  outFile=$1
fi
outFileRaw=${outFile/.json/.raw.json}

docker run --rm -d --name ${dockerName} -p ${port}:5000 stefanoschrs/behance-api

sleep 2

curl localhost:${port}/profile/${username} -o "${outFileRaw}"

node sample.process.js "${outFileRaw}" > "${outFile}"

sleep 2

docker rm -f ${dockerName}
