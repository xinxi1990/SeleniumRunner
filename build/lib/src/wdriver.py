#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,platform,os
reload(sys)
sys.setdefaultencoding('utf8')
from functools import wraps
import time,os,unittest,subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config import *

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


@singleton
class WDriver(object):
    '''
    单例模式
    初始化dirver
    '''

    project_path = os.path.abspath(os.path.dirname(__file__))
    screen_png = os.path.join(project_path, str(time.time()) + "_截图.png")
    driver = None


    def get_platform(self):
        return platform.system()

    def get_driver(self):
        return self.driver


    def get_chrome_driver_path(self):
        if self.get_platform() == "Linux":
           return project_path + "/entity/chromedriver_linux"
        else:
            return project_path + "/entity/chromedriver_mac"

    def init_driver(self,driver_path):
        chrome_options = webdriver.ChromeOptions()
        chrome_options = Options()
        chrome_options.add_argument('--headless') # 不打开浏览器模式
        chrome_options.add_argument('--disable-infobars')  # 不展示chrome控制导航栏
        self.driver = webdriver.Chrome(
            executable_path= driver_path,
            chrome_options=chrome_options)
        self.driver.implicitly_wait(5)
        return self.driver


    def init_hub_drvier(self):
        print("init_hub_drvier")
        driver_path = project_path + self.get_chrome_driver_path()
        print(driver_path)
        os.environ["webdriver.chrome.driver"] = driver_path
        chrome_capabilities = {
            "browserName": "chrome",  # 浏览器名称
            "version": "",  # 操作系统版本
            "platform": "ANY",  # 平台，这里可以是windows、linux、andriod等等
            "javascriptEnabled": True,  # 是否启用js
            "webdriver.chrome.driver": driver_path
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4455/wd/hub", desired_capabilities=chrome_capabilities)
        # hub地址
        print(self.driver)
        self.driver.implicitly_wait(5)
        return self.driver