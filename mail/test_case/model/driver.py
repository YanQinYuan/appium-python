# -*- coding:utf-8 -*-

from appium import webdriver
import globalvar


def drivers():
    """
    根据全局平台参数返回对应的驱动
    :return: WebDriver对象
    """
    desired_caps = {}
    if globalvar.platform == 'ios':
        # 把iOS字典的键/值对更新到desired_caps里
        desired_caps = globalvar.ios_capabilities
    elif globalvar.platform == 'android':
        # 把Android字典的键/值对更新到desired_caps里
        desired_caps = globalvar.android_capabilities
    else:
        pass
    # 配置所需的功能和服务器URL的WebDriver对象
    driver = webdriver.remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
