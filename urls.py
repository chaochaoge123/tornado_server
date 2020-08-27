#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 9:33
# @Author  : qqc
# @File    : urls.py
# @Software: PyCharm


from tornado_server.view import *
from tornado.web import RequestHandler,Application,url
def make_app():
    return Application([
        url(r"/", MainHandler),
        url(r'/ge', Synch)
    ])