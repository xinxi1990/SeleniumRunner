#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,os
import base64
from PIL import Image, ImageGrab
from config import screen_folder
from wdriver import WDriver
from logger import init_logger
logger = init_logger()


class Common():

    @staticmethod
    def print_loggr(text):
        def decorator(func):
            def wrapper(*args, **kw):
                # print('%s():' % (func.__name__))
                logger.info(text)
                f = func(*args, **kw)
            return wrapper
        return decorator


    @staticmethod
    def screen_shot():
        im = ImageGrab.grab()
        current_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        screen_path = os.path.join(screen_folder, current_now + "_screen.png")
        im.save(screen_path)  # 定义保存的路径和保存的图片格式
        return Common.read_file_as_base64(screen_path)

    @staticmethod
    def read_file_as_base64(file_name):
        f = open(file_name, 'rb')
        # 二进制方式打开图文件
        ls_f = base64.b64encode(f.read())
        # 读取文件内容，转换为base64编码
        f.close()
        return ls_f


    @staticmethod
    def auto_screen(func):
        '''截图装饰器
           自动截图装饰器
        '''

        def inner(*args, **kwargs):
            try:
                f = func(*args, **kwargs)
                return f
            except:
                WDriver().get_driver().get_screenshot_as_base64()  # 失败后截图
        return inner