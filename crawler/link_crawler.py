# -*- coding: utf-8 -*-
# 从html中解析a标签的链接

import re
from utils.common import get_html
from database.mysql import MysqlPool


def get_links(html):
    """返回html中的链接 
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    # print(webpage_regex.findall(html), "a 标签列表...")
    return webpage_regex.findall(html)

def link_crawler(seed_url, link_regex):
    """爬取html"""

    crawl_queue = [seed_url]
    while crawl_queue and len(crawl_queue) < 10:
        url = crawl_queue.pop()
        html = get_html(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)
            # crawl_queue.append(link)
    print(crawl_queue, "............")

def saveLinks(links):
    """保存网页链接地址"""
    db = MysqlPool()


    

if __name__ == "__main__":
    # https://www.lagou.com/zhaopin/Node.js/?labelWords=label
    # https://www.lagou.com/zhaopin/Node.js/2/?filterOption=2
    # https://www.lagou.com/zhaopin/Node.js/3/?filterOption=3
    link_crawler('https://www.lagou.com/zhaopin/Node.js/3/?filterOption=3', '^https://www.lagou.com/jobs/\d+.html$')