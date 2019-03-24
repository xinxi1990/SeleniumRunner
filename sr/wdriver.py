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

    driver = None
    _global_wait_time = 5


    def get_platform(self):
        return platform.system()

    def get_driver(self):
        return self.driver

    def init_driver(self,driver_path):
        chrome_options = webdriver.ChromeOptions()
        chrome_options = Options()
        chrome_options.add_argument('--headless') # 不打开浏览器模式
        chrome_options.add_argument('--disable-infobars')  # 不展示chrome控制导航栏
        self.driver = webdriver.Chrome(
            executable_path= driver_path,
            chrome_options=chrome_options)
        self.driver.implicitly_wait(self._global_wait_time)
        return self.driver

