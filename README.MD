# 介绍
基于yaml文件管理测试用例,做selenium自动化测试

# 源码使用
```angularjs
python main.py src --testcase_path /Users/xinxi/PycharmProjects/SeleniumRunner/testcase/test_baidu_fail.yml /
                  --driver_path /Users/xinxi/PycharmProjects/SeleniumRunner/entity/chromedriver_mac
```
#  sr运行
```angularjs
sr --testcase_path /Users/xinxi/PycharmProjects/SeleniumRunner/main.py 
                  --driver_path /Users/xinxi/PycharmProjects/SeleniumRunner/sr/entity/chromedriver_mac
```


# 打包
建立setup.py
python setup.py bdist_egg

# 发布
创建~.pypirc文件
```angularjs
[distutils]
index-servers = pypi

[pypi]
username:你的PyPi用户名
password:你的PyPi密码
```

# 安装上传功能
```
pip install twine
```

# 发布
twine upload dist/*


# 事件列表
```angularjs

```

# 用例编写


# 断言

https://pypi.org/project/PyHamcrest/


# bdd驱动
https://github.com/pytest-dev/pytest-bdd