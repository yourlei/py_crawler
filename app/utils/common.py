# -*-: coding: utf-8 -*-
# 爬虫相关公共函数
import traceback
import requests

def downLoad(url):
    """ 下载网页 """
    # init variable
    code = 0
    html = None
    try:
        html = requests.get(url).text
    except requests.exceptions.ConnectionError:
        print(traceback.format_exc())
        code = 10001
    except requests.exceptions.Timeout:
        print(traceback.format_exc())
        code = 10002

    return code, html
