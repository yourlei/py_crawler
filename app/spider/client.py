# -*- codign: utf-8 -*-
# 模拟客户端应用，发送任务消息
# 相当与生产者
import sys
import getopt
from workers import app

def crawl_task_recent7():
    """ 2019年当当图书畅销榜 top500 """
    base_url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-"

    for page in range(1, 26):
        url = base_url + str(page)
        app.send_task("tasks.best_sale_crawl", args=(url, "day", "7", 2019,))

def crawl_task_by_year(year, category_code, category):
    """ 当当图书年热销top500 
    Args: 
        year: string, 统计年份
        category_code: string, 书本所在分类代码
        category: string, 书本分类名
    """
    base_url = "http://bang.dangdang.com/books/bestsellers/01.%s.00.00.00.00-year-%s-0-1-" % (category_code, year)
    
    # print(base_url)
    for page in range(1, 26):
        url = base_url + str(page)
        app.send_task("tasks.best_sale_crawl", args=(url, "year", year, year, category))

if __name__ == "__main__": 
    pass

    