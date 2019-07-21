# -*- coding: utf-8 -*-
# 启动worker
from task import _celery

if __name__ == "__main__":
    _celery.send_task('task.add', args=(1, 2))