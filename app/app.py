# -*- coding: utf-8 -*-
# app入口

from flask import Flask

# 创建Flask示例
app = Flask(__name__, static_folder='../static')

# 加载配置文件
app.config.from_pyfile('../setting.py')
app.config['JSON_AS_ASCII']

if __name__ == '__main__':
    print(app.config)
