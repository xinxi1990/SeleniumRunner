#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logger import init_logger
logger = init_logger()  # 初始化日志


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
