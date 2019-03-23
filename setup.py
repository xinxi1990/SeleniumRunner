#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: LiangjunFeng
# Mail: zhumavip@163.com
# Created Time:  2018-4-16 19:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "SICA",      #这里是pip项目发布的名称
    version = "2.1.4",  #版本号，数值大的会优先被pip
    keywords = ("pip", "SICA","featureextraction"),
    description = "An feature extraction algorithm",
    long_description = "An feature extraction algorithm, improve the FastICA",
    license = "MIT Licence",

    url = "https://github.com/LiangjunFeng/SICA",     #项目相关文件地址，一般是github
    author = "xinxi",
    author_email = "xinxi1990@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["selenium"]          #这个项目需要的第三方库
)
