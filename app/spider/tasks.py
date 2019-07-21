# -*- coding: utf-8
# 任务处理程序
import os
import csv
import time
from workers import app
from dd_books import parseHtml
from app.utils.utils import MyLog

# ###########################
# define task
# 不需要保存任务结果
# @task(ignore_result=True)
# ###########################

@app.task
def best_sale_crawl(url, classify_code, classify_value, sale_year, category):
    mylog = MyLog()
    books = parseHtml(url)
    
    column = ["rank", "name", "author", "publish_at",\
        "publish_by", "comment_count", "star", "discount_price",\
        "origin_price", "discount", "classify_code",\
        "classify_value", "sale_year", "category"]

    csv_path = os.path.abspath(os.path.dirname(".")) + '/data.csv'
    if not os.path.exists(csv_path):
        with open(csv_path, "a") as f:
            w = csv.writer(f)
            w.writerow(column)
    
    if books and len(books):
        for item in books:
            try:
                row = [item[0], item[1], item[2], item[3], item[4],
                    item[5], item[6], item[7], item[8], item[9], classify_code,
                    classify_value, sale_year, category]
                
                with open(csv_path, "a") as f:
                    w = csv.writer(f)
                    w.writerow(row)
            except Exception as e:
                mylog.logger.error(e)

if __name__ == "__main__":
    pass