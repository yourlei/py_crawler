# from app.setting import celery_broker, celery_backend
from celery import Celery


celery_broker = 'redis://:scut2017@192.168.80.54:6379/1'
celery_backend = 'redis://:scut2017@192.168.80.54:6379/2'

# 创建celery应用实例
# myCelery = Celery('task', broker=celery_broker, backend=celery_backend)

# @myCelery.task()
# def add(x, y):
#     return x + y

""" 创建定时任务 """
myCelery = Celery('add_tasks', broker=celery_broker, backend=celery_backend)
myCelery.conf.update(
    # 配置所在时区 
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    # 官网推荐消息序列化方式为json 
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    # 配置定时任务
    CELERYBEAT_SCHEDULE={
        'my_task': {
            'task': 'task.add',  # task.py模块下的add方法
            'schedule': 10,       # 每隔60s运行一次
            'args': (23, 12),     # add 方法接收的参数
        }
    }
)

@myCelery.task()
def add(x, y):
    return x + y