# -*- coding: utf-8 -*-
# 初始化,创建celery 实例,

from celery import Celery

from setting import redis_host, redis_port, redis_passwd, redis_db_5, redis_db_6

celery_broker = 'redis://%s:%s/%s' % (redis_host, redis_port, redis_db_5)

celery_backend = 'redis://%s:%s/%s' % (redis_host, redis_port, redis_db_6)

# include: 导入的任务模块, worker启动后在导入的模块查找任务
app = Celery('crawler', include=['tasks'], broker='redis://:scut2017@192.168.80.54:6379/3', backend='redis://:scut2017@192.168.80.54:6379/4')
app.conf.update(
    # 配置所在时区 
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    # 官网推荐消息序列化方式为json 
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    # 任务结果保存时间
    # result_expires=3600,
)