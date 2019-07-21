#!/bin/bash
# celery 参数说明
#   Args:
#     -A app所在的文件模块
#     worker: 以worker方式运行
#     -l: 日志等级
celery -A tasks worker --loglevel=info