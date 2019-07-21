# coding: utf-8
# 爬去当当网热销图书数据
import re
from bs4 import BeautifulSoup
from app.utils.common import downLoad
from app.utils.utils import MyLog

mylog = MyLog()

def parseHtml(url: str):
    """解析html,提取页面内容
    """
    books_list = []
    code, html = downLoad(url)

    if code:
        return None

    try:
        soup = BeautifulSoup(html, "lxml")
        # 获取网页中的畅销书信息
        book_list = soup.find('ul', class_="bang_list clearfix bang_list_mode")('li')
    except Exception as e:
        mylog.logger.warn(url)
        mylog.logger.error(e)
        raise e
    
    for item in book_list:
        info = item.find_all("div")

        rank = info[0].text[0:-1] # 热销榜排名
        name = info[2].text # 书名
        comment_star = re.findall(r'[0-9\.]+', info[3].text) # 用户评论数和推荐指数
        author = info[4].text.replace("\u3000", " ") # 作者
        publish_info = info[5].text.split(" ") # ['2019-01-10', '人民出版社'] 出版时间及出版社
        price_info = re.findall(r'[0-9\.]+', info[6].find_next("p").text) # 价格折扣信息
        
        try:
            books_list.append([
                rank,
                name,
                author,
                publish_info[0],
                publish_info[1],
                comment_star[0],
                comment_star[1],
                price_info[0],
                price_info[1],
                price_info[2]
            ])
        except Exception as e:
            mylog.logger.error(e)
      # 类选择器效率相对较慢
      # rank = item.select(".list_num")[0].text[0:-1]
      # print(rank)
    return books_list

def get_book_category():
    """ 提取畅销榜页面左侧图书分类代码 """
    """图书畅销榜url后缀分析:
    近七日畅销榜：　　01.00.00.00.00.00-recent7-0-0-1-1
    童书近七日畅销榜：01.41.00.00.00.00-recent7-0-0-1-1
    对比可知41即代表图书分类码
    """
    url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1"
    code, html = downLoad(url)

    if code:
        return None
    
    soup = BeautifulSoup(html, "lxml")
    nav_box = soup.find(id="sortRanking")("a")

    for item in nav_box:
        category_code = re.findall(r'\d{2}\.+', str(item))
        category_text = item.text
        category_code = category_code[1][0:-1] if len(category_code) > 2 else None
        # 保存到txt
        input = open('category.txt', "a")
        input.write(category_code + "," + category_text + "\n")
        input.close()

if __name__ == "__main__":
    # get_book_category()
    pass