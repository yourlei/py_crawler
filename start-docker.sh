#!/bin/bash

sudo docker run -dit \
--name db2es_A1 \
-p 18092:8095 \
-v $PWD:/var/www/db2es \
-w /var/www/db2es \
python:3.6-slim 