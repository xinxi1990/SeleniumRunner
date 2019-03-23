#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,platform,os
reload(sys)
sys.setdefaultencoding('utf8')
from functools import wraps
import time,os,unittest,subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import init_logger
from common import Common
from wdriver import WDriver
logger = init_logger()

class Location():

    def __init__(self,driver):
        self.driver = driver

    def location_element(self,location):
        '''
        解析定位方法
        :param driver:
        :param location:
        :return:
        '''
        method = str(location).split(",")[0]
        value = str(location).split(",")[1]
        if method == "By.NAME":
            return self.driver.find_element(By.NAME, value)
        elif method == "By.ID":
            return self.driver.find_element(By.ID, value)
        elif method == "By.CLASS_NAME":
            return self.driver.find_element(By.CLASS_NAME, value)
        elif method == "By.XPATH":
            return self.driver.find_element(By.XPATH, value)
        elif method == "By.CSS_SELECTOR":
            return self.driver.find_element(By.CSS_SELECTOR, value)
        elif method == "By.LINK_TEXT":
            return self.driver.find_element(By.LINK_TEXT, value)
        elif method == "By.PARTIAL_LINK_TEXT":
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif method == "By.TAG_NAME":
            return self.driver.find_element(By.TAG_NAME, value)


    # @Common.print_loggr("显示等待定位元素")
    def create_location(self,location):
        method = str(location).split(",")[0]
        value = str(location).split(",")[1]
        if method == "By.NAME":
            return (By.NAME, value)
        elif method == "By.ID":
            return (By.ID, value)
        elif method == "By.CLASS_NAME":
            return (By.CLASS_NAME, value)
        elif method == "By.XPATH":
            return (By.XPATH, value)
        elif method == "By.CSS_SELECTOR":
            return (By.CSS_SELECTOR, value)
        elif method == "By.LINK_TEXT":
            return (By.LINK_TEXT, value)
        elif method == "By.PARTIAL_LINK_TEXT":
            return (By.PARTIAL_LINK_TEXT, value)
        elif method == "By.TAG_NAME":
            return (By.TAG_NAME, value)


    @Common.print_loggr("打开浏览器")
    def open_url(self,url):
        self.driver.get(url)


    def switch_frame(self):
        '''
        切换frame
        :return:
        '''
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])

    def switch_windows(self):
        '''
        切换窗口
        :return:
        '''
        handles_list = self.driver.window_handles
        self.driver.switch_to.window(str(handles_list[-1]))


    def display_wait(self,time,loc):
        '''
        显示等待
        :param time:
        :param loc:
        :return:
        '''
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            logger.error("显示等待元素超时:{}".format(loc))
            return None


    def scroll_down(self):
        js="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def scroll_top(self):
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)

    @Common.print_loggr("关闭浏览器")
    def close_brower(self):
        self.driver.quit()


    def when_element_click(self,time,loc):
        '''
        当元素存在则点击
        :return:
        '''
        _loc = self.create_location(loc)
        _el = self.display_wait(time, *_loc)
        if _el != None:
           _el.click()
           logger.info("存在元素并点击:{}".format(_loc))
        else:
           logger.info("不存在元素:{}".format(_loc))





    def assert_element(self):
        '''
        断言元素
        :return:
        '''
        pass