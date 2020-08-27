#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 9:33
# @Author  : qqc
# @File    : urls.py
# @Software: PyCharm


from view import *
from tornado.web import RequestHandler, Application, url
from settings import setings

url_list = [
    url(r"/", MainHandler),
    url(r'/ge', Synch)
]

make_app = Application(
    url_list, **setings)


# make_app.add_handlers('https://www.qqc-home.com', url_list)
