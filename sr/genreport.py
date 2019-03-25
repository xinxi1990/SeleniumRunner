#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,re,time,subprocess,sys,jinja2,requests,json
from jinja2 import Environment, PackageLoader
from config import report_folder



class GenReport():


    def __init__(self,test_result):
        self.test_result = test_result


    def _create_result_data(self):
        result_data = {}
        result_data["testPass"] = "1"
        result_data["testResult"] = self.test_result
        result_data["testName"] = "1"
        result_data["testAll"] = "1"
        result_data["testFail"] = "1"
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
            if not os.path.exists(report_folder):
                os.mkdir(report_folder)
                print('创建report文件夹!{}'.format(report_folder))
            with open(report_path, "wb") as f:
                f.write(html_content.encode("utf-8"))
                print('写入结果{}完成!'.format(report_path))
        except Exception as e:
            print('组装体检结果异常!{}'.format(e))
        finally:
            return report_path

if __name__ == '__main__':
    GenReport().render_reprot()