#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging,os,time
from logzero import setup_logger

root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
logger_folder = os.path.join(root_path,"logger")


def get_current_time():
    '''
    获取当前时间戳
    :return:
    '''
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return current_time


def init_logger():
    '''
    初始化日志
    :return:
    '''
    if not os.path.exists(logger_folder):
        os.mkdir(logger_folder)
    logger_file = os.path.join(logger_folder,"logger.log")
    logger = setup_logger(name="logger", logfile=logger_file, level=logging.INFO)
    return logger

