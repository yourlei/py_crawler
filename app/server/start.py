# -*- coding: utf-8 -*-
# api 入口
from app.app import app

@app.route("/")
def index():
    return 'hello world'


def run(host='0.0.0.0', port=8095, debug=False):
    """运行服务
    Args:
        host: 默认值0.0.0.0, 允许外部访问
        port: 端口号, default 8095
        debug: 调试模式,default: False
        version: 服务版本号, default: v1.0
    """
    app.run(host=host, port=port, debug=debug)
