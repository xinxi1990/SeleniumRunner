#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,re,time,subprocess,sys,jinja2,requests,json
from jinja2 import Environment, PackageLoader
from config import report_folder
from logger import init_logger
logger = init_logger()


class GenReport():


    def __init__(self,sucess_size,fail_size,test_result):
        self.sucess_size = sucess_size
        self.fail_size = fail_size
        self.test_result = test_result


    def _create_result_data(self):
        result_data = {}
        result_data["testPass"] = self.sucess_size
        result_data["testResult"] = self.test_result
        result_data["testName"] = "AutoTest"
        result_data["testAll"] = self.sucess_size + self.fail_size
        result_data["testFail"] = self.fail_size
        result_data["beginTime"] =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        result_data["totalTime"] = "100ms"
        result_data["testSkip"] = 0
        return result_data


    def render_reprot(self,**params):
        '''
        jinja2渲染结果
        :return:
        '''
        db = None
        try:
            env = Environment(loader=PackageLoader('sr', 'template'))
            template = env.get_template("template.html")
            html_content = template.render(result_data=self._create_result_data())
            current_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
            report_path = os.path.join(report_folder, current_now + "_result.html")
            with open(report_path, "wb") as f:
                f.write(html_content.encode("utf-8"))
                logger.info('报告地址:\n{}'.format(report_path))
        except Exception as e:
            logger.error('生成报告异常!{}'.format(e))
        finally:
            return report_path

