# -*- coding: utf-8 -*-
# 从html中解析a标签的链接

import re
from common import get_html

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
            # print(link, '///////////')
            # if re.match(link_regex, link):
            #     crawl_queue.append(link)
            crawl_queue.append(link)
    print(crawl_queue, "............")

if __name__ == "__main__":
    link_crawler('https://www.lagou.com/zhaopin/Node.js/?labelWords=label', '/(index|view)')