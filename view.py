#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 9:33
# @Author  : qqc
# @File    : view.py
# @Software: PyCharm


from tornado.ioloop import IOLoop
from tornado.web import RequestHandler,Application,url
from tornado.httpclient import HTTPClient
from tornado.httpserver import HTTPServer
import requests
import redis


class MainHandler(RequestHandler):
    print(RequestHandler.head,"tttttttttttt")
    def get(self):
        name = self.get_query_argument('name')
        if name:
            self.write("Hello,{0}".format(name))
        else:
            self.send_error(409, msg="异常错误")


class Synch(RequestHandler):
    def get(self):
        response = requests.get('https://www.qqc-home.com/t_gevent')
        self.write(response.json())


class FactorialService(RequestHandler):
    redis.Redis(host="")
    pass