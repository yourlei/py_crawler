# -*-: coding: utf-8 -*-
# 工具库
import os
import sys
import logging

class MyLog():
    """ 日志模块 """
    logging_format = logging.Formatter(
      '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    
    def __init__(self):
        f_handler = logging.FileHandler("my.log")
        f_handler.setFormatter(self.logging_format)
        self.logger = logging.getLogger()
        self.logger.addHandler(f_handler)

if __name__ == "__main__":
    # mylog = MyLog()
    # try:
    #   a = 2 / 0
    # except Exception as e:
    #   mylog.logger.error(e)
    print(os.path.dirname(os.path.realpath(__file__)) +'/user_dict.txt')
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print(os.path.abspath(os.path.join(os.getcwd())))