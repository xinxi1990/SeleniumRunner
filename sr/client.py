#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,os
import time,yaml,sys,getopt,unittest
from wdriver import WDriver
from location import Location
from logger import init_logger
from config import report_folder
logger = init_logger()


class MainTest(unittest.TestCase):


    def __init__(self, methodName='runTest', param=None):
        super(MainTest, self).__init__(methodName)
        testcase_path = param["testcase_path"]
        self.driver_path = param["driver_path"]
        global testcase_path
        global driver_path



    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.location = None
        logger.info("初始化环境")
        cls.case_info = cls.load_case_file(testcase_path)
        global driver
        global location
        global case_info


    def setUp(self):
        logger.info("开始测试")


    @staticmethod
    def load_case_file(file_path):
        with open(file_path) as f:
            file_str = yaml.load(f)
        return  file_str


    def test_case(self):
        logger.info("加载测试用例")
        yaml_output = self.case_info
        case_list = dict(yaml_output).keys()
        for test_case in case_list:
            if test_case != 'name':
                try:
                    driver = WDriver().init_driver(self.driver_path)
                except Exception as  e:
                    if driver == None:
                        driver = WDriver().get_driver()
                location = Location(driver)
                for case_step in yaml_output[test_case]:
                    try:
                        if case_step['action'] == "open_brower":
                           location.open_brower(case_step['location'])
                           location.wait_sleep(case_step["time"])
                        elif case_step['action'] == "click":
                            element = location.create_location(case_step['location'])
                            location.display_wait(case_step["time"],element).click()
                        elif case_step['action'] == "send_keys":
                            element = location.create_location(case_step['location'])
                            location.display_wait(case_step["time"], element).send_keys(case_step['text'])
                        elif case_step['action'] == "switch_to_frame":
                            location.wait_sleep(case_step["time"])
                            location.switch_frame()
                        elif case_step['action'] == "switch_windows":
                            location.switch_windows()
                        elif case_step['action'] == "scroll_down":
                            location.scroll_down()
                        elif case_step['action'] == "scroll_top":
                            location.scroll_top()
                        elif case_step['action'] == "when_element_click":
                            element = location.create_location(case_step['location'])
                            location.when_element_click(case_step["time"],element)
                    except Exception as e:
                        logger.error("加载测试用例异常:{}".format(e))
                location.close_brower()
        print(len(location.get_base64_image_list()))
        base64_image_list = location.get_base64_image_list()
        global base64_image_list

    @classmethod
    def tearDownClass(cls):
        logger.info("结束全部测试")


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

    runner = unittest.TextTestRunner()
    runner.run(suite)
    #debug模式

    # from HTMLTestRunner_cn.HTMLTestRunner_cn import HTMLTestRunner
    # current_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # report_filename = os.path.join(report_folder, current_now + "_result.html")
    # fp = open(report_filename, 'wb')
    # runner = HTMLTestRunner(
    #     stream=fp,
    #     title=u'SeleniumRunner自动化执行报告',
    #     description=u'用例执行情况:',
    #     verbosity=2, retry=0, save_last_try=True)
    # # verbosity表示报告级别
    # # retry表示失败重试机制
    # runner.run(suite)
    # fp.close()







