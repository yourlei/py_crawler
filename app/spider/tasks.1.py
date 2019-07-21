# -*- coding: utf-8
# 任务处理程序
import os
import time
from workers import app
from dd_books import parseHtml
from app.utils.mysql_pool import MysqlPool
from app.utils.utils import MyLog

# ###########################
# define task
# 不需要保存任务结果
# @task(ignore_result=True)
# ###########################

# db = MysqlPool()

@app.task
def best_sale_crawl(url, classify_code, classify_value, sale_year, category):
    mylog = MyLog()
    books = parseHtml(url)
    
    # start = time.time()
    csv_path = os.path.abspath(os.path.dirname(".")) + '/data.csv'
    if books and len(books):
        # sql = "insert into best_sale_books(rank, name, author, publish_at, publish_by,\
        #     comment_count, star, discount_price, origin_price, discount, classify_code,\
        #     classify_value, sale_year, category) values"
        # rows = []
        for item in books:
        #     record = "(" + item[0] + ",'" + item[1] + "','" + item[2] + "','" + item[3]\
        #         + "','" + item[4] + "'," + item[5] + ",'" + item[6]\
        #         + "','" + item[7] + "','" + item[8] + "','" + item[9]\
        #         + "','" + classify_code + "','" + classify_value + "',"\
        #         + sale_year + ",'" + category + "')"
        #     rows.append(record)
        # sql = sql + ','.join(rows)
        # try:
        #     db.cur.execute(sql)
        #     db.conn.commit()
        # except Exception as e:
        #     print("insert error")
        #     db.conn.rollback()
        #     db.conn.commit()
        #     raise e
            try:
                line = item[0] + "," + item[1] + "," + item[2] + "," + item[3]\
                + "," + item[4] + "," + item[5] + "," + item[6]\
                + "," + item[7] + "," + item[8] + "," + item[9]\
                + "," + classify_code + "," + classify_value + ","\
                + sale_year + "," + category

                input = open(csv_path, "a")
                input.write(line + "\r")
                input.close()
            except Exception as e:
                mylog.logger.error(e)
            

    # print("cost: ", time.time() - start)

if __name__ == "__main__":
    log = MyLog()
    log.logger.error("dkjfdl")
    pass