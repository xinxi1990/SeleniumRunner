#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,os
import time,yaml,sys,getopt,unittest
from wdriver import WDriver
from location import Location
from logger import init_logger
from config import report_folder
from HTMLTestRunner_cn.HTMLTestRunner_cn import HTMLTestRunner
logger = init_logger()


class MainTest(unittest.TestCase):


    def __init__(self, methodName='runTest', param=None):
        super(MainTest, self).__init__(methodName)
        global testcase_path
        global driver_path
        testcase_path = param["testcase_path"]
        driver_path = param["driver_path"]



    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.location = None
        logger.info("*****初始化环境*****")
        cls.case_info = cls.load_case_file(testcase_path)
        global driver
        global location
        global case_info


    def setUp(self):
        logger.info("*****开始测试*****")


    @staticmethod
    def load_case_file(file_path):
        with open(file_path) as f:
            file_str = yaml.load(f)
        return  file_str


    def test_case(self):
        yaml_output = self.case_info
        case_list = dict(yaml_output).keys()
        for test_case in case_list:
            if test_case != 'name':
                driver = WDriver().init_driver(driver_path)
                location = Location(driver)
                for case_step in yaml_output[test_case]:
                    if case_step['action'] == "get":
                       location.open_url(case_step['location'])
                       time.sleep(case_step["time"])
                    elif case_step['action'] == "click":
                        element = location.create_location(case_step['location'])
                        location.display_wait(case_step["time"],element).click()
                    elif case_step['action'] == "send_keys":
                        element = location.create_location(case_step['location'])
                        location.display_wait(case_step["time"], element).send_keys(case_step['text'])
                    elif case_step['action'] == "switch_to_frame":
                        time.sleep(case_step["time"])
                        location.switch_frame()
                    elif case_step['action'] == "switch_windows":
                        location.switch_windows()
                    elif case_step['action'] == "scroll_down":
                        location.scroll_down()
                    elif case_step['action'] == "scroll_top":
                        location.scroll_top()
                    elif case_step['action'] == "scroll_top":
                        location.scroll_top()
                location.close_brower()




    @classmethod
    def tearDownClass(cls):
        logger.info("*****结束全部测试*****")


    def main_run_back():
        opts, args = getopt.getopt(sys.argv[1:], '-h-f:', ['help', 'filepath='])
        fileName = None
        for opt_name, opt_value in opts:
            if opt_name in ('-h', '--help'):
                logger.info("帮助")
                exit()
            if opt_name in ('-f', '--filepath'):
                fileName = opt_value
                logger.info("用例路径:" + fileName)

        suite = unittest.TestSuite()
        suite.addTest(Main('test_case'))
        runner = unittest.TextTestRunner()
        runner.run(suite)




def main_run():
    parser = argparse.ArgumentParser(
        description='Selenium Testing')
    parser.add_argument(
        '--testcase_path',
        help="测试集路径")
    parser.add_argument(
        '--driver_path',
        help="chrome driver路径")

    args = parser.parse_args()
    testcase_path = str(args.testcase_path)
    driver_path = str(args.driver_path)
    print("\033[0;32m{0}\033[0m".format(testcase_path))
    print("\033[0;32m{0}\033[0m".format(driver_path))
    suite = unittest.TestSuite()
    param = {}
    param['testcase_path'] = testcase_path
    param['driver_path'] = driver_path
    suite.addTest(MainTest('test_case',param=param))

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # debug模式

    current_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    report_filename = os.path.join(report_folder, current_now + "_result.html")
    fp = open(report_filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'SeleniumRunner自动化执行报告',
        description=u'用例执行情况:',
        verbosity=2, retry=0, save_last_try=True)
    # verbosity表示报告级别
    # retry表示失败重试机制
    runner.run(suite)
    fp.close()




