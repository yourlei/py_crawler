# -*- coding: utf-8 -*-
#
# 安装程序
from distutils.core import setup


LONG_DESCRIPTION = """
爬虫程序
""".strip()

SHORT_DESCRIPTION = """
python3 爬虫程序""".strip()

DEPENDENCIES = [
  'PyMySQL',
  'DBUtils'
]

VERSION = '1.0'
URL = 'https://github.com/yourlei/py_crawler'

setup(
    name='python3 scrap',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,

    author='leiyu',
    author_email='yourlin127@gmail.com',
    license='Apache Software License',

    keywords='crawler python3',

    packages=[
      'crawler',
      'crawler.database',
    ],
)
