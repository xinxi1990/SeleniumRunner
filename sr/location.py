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
success_info_list = []
fail_info_list = []

class Location():

    def __init__(self,driver,case_name,description):
        self.driver = driver
        self.case_name = case_name
        self.description = description


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
            fail_detail = "location_element Exception:{}".format(e)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name, fail_detail=fail_detail)
            raise Exception



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
            fail_detail = "create_location Exception:{}".format(location)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name, fail_detail=fail_detail)
            raise Exception



    @Common.print_loggr("打开浏览器")
    def open_brower(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            fail_detail = "open_brower Exception:{}".format(url)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name, fail_detail=fail_detail)
            raise Exception


    @Common.print_loggr("关闭浏览器")
    def close_brower(self):
        try:
            self.driver.close()
        except Exception as e:
            fail_detail = "关闭浏览器异常:{}".format(e)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name, fail_detail=fail_detail)
            raise Exception


    def switch_frame(self):
        '''
        切换frame
        :return:
        '''
        try:
            self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
        except Exception as e:
            fail_detail = "switch_frame Exception:{}".format(e)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name, fail_detail=fail_detail)
            raise Exception



    def switch_windows(self):
        '''
        切换窗口
        :return:
        '''
        try:
            handles_list = self.driver.window_handles
            self.driver.switch_to.window(str(handles_list[-1]))
        except Exception as e:
            fail_detail = "switch_windows Exception:{}".format(e)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name, fail_detail=fail_detail)
            raise Exception

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
            fail_detail = "display_wait Exception:{}".format(loc)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name,fail_detail=fail_detail)
            raise Exception


    def scroll_down(self):
        try:
            js="window.scrollTo(0,document.body.scrollHeight)"
            self.driver.execute_script(js)
        except Exception as e:
            fail_detail = "scroll_down Exception:{}".format(e)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name,fail_detail=fail_detail)
            raise Exception


    def scroll_top(self):
        try:
            js="window.scrollTo(0,0)"
            self.driver.execute_script(js)
        except Exception as e:
            fail_detail = "scroll_top Exception:{}".format(e)
            logger.error(fail_detail)
            self.create_fail_info(case_name=self.case_name,fail_detail=fail_detail)
            raise Exception



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
        return self.driver.get_screenshot_as_base64()


    def get_base64_image_list(self):
        return base64_image_list

    def get_fail_info_list(self):
        return fail_info_list

    def get_success_info_list(self):
        return success_info_list


    def wait_sleep(self,wait_time):
        time.sleep(int(wait_time))


    def create_fail_info(self,**kwargs):
        '''
        组装测试异常数据
        :return:
        '''
        fail_info = {}
        fail_info["methodName"] = kwargs['case_name']
        fail_info["description"] = self.description
        fail_info["spendTime"] = "10ms"
        fail_info["status"] = "FAIL"
        fail_image =  "<img src=\"data:image/png;base64,{}\"/>".format(self.screenshot_as_base64())
        fail_info["log"] =  [kwargs['fail_detail'],fail_image]
        fail_info_list.append(fail_info)
        global fail_info_list


    def create_success_info(self):
        '''
        组装测试异常数据
        :return:
        '''
        success_info = {}
        success_info["methodName"] = self.case_name
        success_info["description"] = self.description
        success_info["spendTime"] = "10ms"
        success_info["status"] = "SUCCESS"
        success_info["log"] =  []
        success_info_list.append(success_info)
        global success_info_list