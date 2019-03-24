#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,platform
reload(sys)
sys.setdefaultencoding('utf8')
import time,os,unittest,subprocess
from functools import wraps
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import init_logger
from common import Common
from wdriver import WDriver
from exception import LocationError
logger = init_logger()

base64_image_list = []
fail_info_list = []


class Location():

    def __init__(self,driver,case_name):
        self.driver = driver
        self.case_name = case_name


    def location_element(self,location):
        '''
        解析定位方法
        :param driver:
        :param location:
        :return:
        '''
        try:
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
        except Exception as e:
            logger.info("捕获异常:{}".format(e))
            base64_image_list.append(self.screenshot_as_base64())
            global base64_image_list



    # @Common.print_loggr("显示等待定位元素")
    def create_location(self,location):
        try:
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
        except Exception as e:
            logger.info("捕获异常:{}".format(e))
            fail_info = {}
            fail_info["case_name"] = self.case_name
            fail_info["fail_info"] = self.screenshot_as_base64()
            # base64_image_list.append(self.screenshot_as_base64())
            # global base64_image_list
            fail_info_list.append(fail_info)
            global fail_info_list



    @Common.print_loggr("打开浏览器")
    def open_brower(self,url):
        self.driver.get(url)


    @Common.print_loggr("关闭浏览器")
    def close_brower(self):
        self.driver.close()


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
            fail_info = {}
            fail_info["case_name"] = self.case_name
            ail_info["fail_info"] = "显示等待元素超时:{}".format(loc)
            fail_info["fail_sceenshot"] = self.screenshot_as_base64()
            # base64_image_list.append(self.screenshot_as_base64())
            # global base64_image_list
            fail_info_list.append(fail_info)
            global fail_info_list



    def scroll_down(self):
        js="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def scroll_top(self):
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)

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



    def screenshot_as_base64(self):
        '''
        base64位截图
        :return:
        '''
        logger.info("截取当前错误")
        return self.driver.get_screenshot_as_base64()


    def get_base64_image_list(self):
        return base64_image_list

    def get_fail_info_list(self):
        return fail_info_list


    def wait_sleep(self,wait_time):
        time.sleep(int(wait_time))

