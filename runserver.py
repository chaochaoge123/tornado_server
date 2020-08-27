#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 15:48
# @Author  : qqc
# @File    : runserver.py
# @Software: PyCharm


from tornado.ioloop import IOLoop
from tornado.web import RequestHandler,Application,url
from tornado.httpclient import HTTPClient
from tornado.httpserver import HTTPServer
import requests
import redis
from urls import make_app


if __name__ == '__main__':
    http_server = HTTPServer(make_app)
    http_server.listen(8888)
    IOLoop.current().start()
