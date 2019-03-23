#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 创建driver
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os,sys,subprocess,pytest,time,allure,base64
from allure.constants import AttachmentType
from config import screen_folder
from wdriver import WDriver
sys.path.append('..')
from logger import init_logger
logger = init_logger()  # 初始化日志


# 当设置autouse为True时,
# 在一个session内的所有的test都会自动调用这个fixture
@pytest.fixture()
def driver_setup(request):
    logger.info("自动化测试开始!")
    request.instance.driver = WDriver().init_driver()
    logger.info("driver初始化")
    def driver_teardown():
        logger.info("自动化测试结束!")
        request.instance.driver.quit()
    request.addfinalizer(driver_teardown)



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        logger.info("测试失败了")
        with allure.step('添加失败截图...'):
            allure.attach(rep.nodeid, WDriver().get_driver().get_screenshot_as_png(),type=AttachmentType.PNG)







