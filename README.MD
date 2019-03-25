# 介绍
基于yaml文件管理测试用例,做selenium自动化测试

# 源码运行
```angularjs
python main.py sr --testcase_path /Users/xinxi/PycharmProjects/SeleniumRunner/testcase/test_baidu_fail.yml /
                  --driver_path /Users/xinxi/PycharmProjects/SeleniumRunner/entity/chromedriver_mac
```
#  安装包运行
```angularjs
sr --testcase_path /Users/xinxi/PycharmProjects/SeleniumRunner/main.py /
                  --driver_path /Users/xinxi/PycharmProjects/SeleniumRunner/sr/entity/chromedriver_mac
```


# 多用例执行
```angularjs
python main.py sr --testcase_path /Users/xinxi/PycharmProjects/SeleniumRunner/testcase /
                --driver_path /Users/xinxi/PycharmProjects/SeleniumRunner/entity/chromedriver_mac

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

## 打开网站
```angularjs
action: "open_brower"
location: "http://www.baidu.com"
time: 1
```
## 点击元素
```angularjs
action: "click"
location: "By.CLASS_NAME,account-tab-account"
time: 1
```

## 输入文字
```angularjs
action: "send_keys"
location: "By.ID,kw"
text: "test selenium"
time: 1
```

## 切换frame
```angularjs
action: "switch_to_frame"
```

## 切换窗体
```angularjs
action: "switch_windows"
```



## 向上滑动
```angularjs
action: "scroll_top"
```

## 向下滑动
```angularjs
action: "scroll_down"
```


# 用例编写
```
name: "test for douban"
test_case_1:
  - action: "open_brower"
    location: "http://www.douban.com"
    time: 1
  - action: "switch_to_frame"
    time: 1
  - action: "click"
    location: "By.CLASS_NAME,account-tab-account"
    time: 1
  - action: "send_keys"
    location: "By.CLASS_NAME,account-form-input"
    text: "18513571170"
    time: 1
  - action: "send_keys"
    location: "By.CLASS_NAME,password"
    text: "11111"
    time: 1
```


# 断言

https://pypi.org/project/PyHamcrest/


# bdd驱动
https://github.com/pytest-dev/pytest-bdd