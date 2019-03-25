#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,os
import time,yaml,sys,getopt,unittest
from wdriver import WDriver
from location import Location
from logger import init_logger
from config import report_folder
from genreport import GenReport
logger = init_logger()

total_base64_image_list = []

class MainTest(unittest.TestCase):


    def __init__(self, methodName='runTest', param=None):
        logger.info("初始化环境")
        super(MainTest, self).__init__(methodName)
        testcase_path = param["testcase_path"]
        self.driver_path = param["driver_path"]
        self.case_info = MainTest.load_case_file(testcase_path)



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
            case_name = yaml_output["name"]
            if test_case != 'name':
                try:
                    driver = WDriver().init_driver(self.driver_path)
                except Exception as  e:
                    if driver == None:
                        driver = WDriver().get_driver()
                location = Location(driver,case_name)
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

        GenReport(location.get_fail_info_list()).render_reprot()






def main_run():
    logger.warning("*****************************************************************")
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
    if os.path.isdir(testcase_path):
       for file in os.listdir(testcase_path):
           testcase_file = os.path.join(testcase_path,file)
           logger.info(testcase_file)
           param = {}
           param['testcase_path'] = testcase_file
           param['driver_path'] = driver_path
           suite.addTest(MainTest('test_case', param=param))

    elif os.path.isfile(testcase_path):
        param = {}
        param['testcase_path'] = testcase_path
        param['driver_path'] = driver_path
        suite.addTest(MainTest('test_case', param=param))

    test_count = suite.countTestCases()
    logger.info("本次共执行:{}组测试用例".format(test_count))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #debug模式

    logger.warning("*****************************************************************")








