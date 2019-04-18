#!/bin/bash
# 
# 创建容器

sudo docker run -dti \
  --name scrap_py3 \
  -v "$PWD":/var/www/code \
  -w /var/www/code \
  python:3.6-slim