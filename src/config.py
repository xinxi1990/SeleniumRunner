#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
配置文件
"""
import os,time

project_path = os.path.abspath(os.path.dirname(__file__))
screen_folder = os.path.join(project_path,"screen")
report_folder = os.path.join(project_path,"report")
if not os.path.exists(screen_folder):
    os.mkdir(screen_folder)
    print("\033[0;32m{0}\033[0m".format("创建截图文件夹:".format(screen_folder)))
if not os.path.exists(report_folder):
    os.mkdir(report_folder)
    print("\033[0;32m{0}\033[0m".format("创建报告文件夹:".format(report_folder)))

screen_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
screen_png = os.path.join(screen_folder, str(screen_time + "_截图.png"))

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

chrome_driver_path = PATH("../entity/chromedriver_mac")