# -*- coding: utf-8 -*-
# 
import urllib.request
import urllib.robotparser as robotparser
import urllib.parse as urlparse

def get_html(url, num_retries=2):
    """抓取html内容
    """
    print("downloading html...")
    try:
        req = urllib.request.Request(url)
        req.add_header('Referer', 'http://www.python.org/')
        # Customize the default User-Agent header value:
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
        html = urllib.request.urlopen(req).read()
    except urllib.request.HTTPError as e:
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = get_html(url, num_retries-1)

    return html.decode("utf-8")

def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp

if __name__ == "__main__":
    html = get_html("https://www.lagou.com/zhaopin/Node.js/?labelWords=label")
    # rp = get_robots("http://shaoguan.baixing.com/xinfangchushou")
    # header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    # flag = rp.can_fetch("*", "http://shaoguan.baixing.com/xinfangchushou")
    # print(flag)
    str = html.decode("utf-8")
    print(str)
    pass