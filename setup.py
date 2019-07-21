# -*- coding: utf-8 -*-
#
from distutils.core import setup
LONG_DESCRIPTION = """
当当爬虫
""".strip()
SHORT_DESCRIPTION = """
当当爬虫""".strip()
DEPENDENCIES = [
  "jsonschema",
  "redis",
  "requests",
  "Flask",
  "PyMySQL",
  "DBUtils",
  "celery",
  "beautifulsoup4",
  "lxml"
]
VERSION = '1.0'
URL = ''
setup(
    name='当当热销榜爬虫',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author='leiyu',
    author_email='yourlin127@gmail.com',
    license='Apache Software License',
    keywords='python, flask',
    packages=[
      'app',
      'app.celery',
      'app.server',
      'app.spider',
      'app.utils',
    ],
)
