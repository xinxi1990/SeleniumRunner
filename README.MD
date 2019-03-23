# 介绍
基于yaml文件管理测试用例,做selenium自动化测试

# 使用
```angularjs
python main.py sr  /Users/xinxi/PycharmProjects/SeleniumRunner/testcase/test_douban.yml
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
