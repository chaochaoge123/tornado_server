#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 13:54
# @Author  : qqc
# @File    : settings.py
# @Software: PyCharm


setings = {
    'template_path': 'templates',  # 配置模板路径
    'static_path': 'static',  # 配置静态文件存放的路径
    'static_url_prefix': '/zhanggen/',  # 在模板中引用静态文件路径时使用的别名 注意是模板引用时的别名
    "xsrf_cookies": True,  # 使用xsrf认证
    'cookie_secret': 'xsseffekrjewkhwy'  # cokies加密时使用的盐
}
