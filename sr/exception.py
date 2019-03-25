#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from logger import init_logger
logger = init_logger()


try:
    FileNotFoundError = FileNotFoundError
except NameError:
    FileNotFoundError = IOError

try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError

class MyBaseError(BaseException):
    pass

class FileFormatError(MyBaseError):
    pass

class ParamsError(MyBaseError):
    pass

class ResponseError(MyBaseError):
    pass

class ParseResponseError(MyBaseError):
    pass

class ValidationError(MyBaseError):
    pass

class NotFoundError(MyBaseError):
    pass

class FunctionNotFound(NotFoundError):
    pass

class VariableNotFound(NotFoundError):
    pass

class ApiNotFound(NotFoundError):
    pass

class SuiteNotFound(NotFoundError):
    pass

class TestcaseNotFound(NotFoundError):
    pass


class BaseError(Exception):
    def __init__(self):
        self.err_msg = ''
        self.err_msg_detail = ''

class LocationError(BaseError):
    def __init__(self, err_msg):
        self.err_msg = {'code': 70011, 'message': '请求参数错误'}
        self.err_msg_detail = "请求参数错误" + err_msg
        logger.error(self.err_msg_detail)
        Exception.__init__(self, self.err_msg, self.err_msg_detail)


