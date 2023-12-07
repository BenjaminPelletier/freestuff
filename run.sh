#!/bin/bash

docker image build -t freestuff .
docker container run -p 8090:8090 freestuff
