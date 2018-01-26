# -*- coding:utf-8 -*-
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# 项目绝对路径
global_path = 'D:/istl/po-sample-python'

# 服务器URL
server_url = 'http://localhost:4723/wd/hub'

# 配置iOS的参数
ios_capabilities = {
    'platformName': 'ios',
    'deviceName': 'iPhone 6s',
    'app': 'ios-app-bootstrap.app',
}

# 配置Android的参数
android_capabilities = {
    'platformName': '5.1.1',
    'platformName': 'android',
    'deviceName': '192.168.58.101:5555',
    'app': PATH(
            'D:/istl/android-debug.apk'
        )
}

# 测试平台（android/ios）
platform = 'android'
