# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '6',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.tencent.wework',  # 启动APP Package名称
    'appActivity': '.launch.LaunchSplashActivity',  # 启动Activity名称，如被测的页面
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True，是否需要输入非英文之外的语言
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 是否在测试前后重置相关环境，true则为不重置，如登录信息、权限设置。fullReset
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'  # 引擎，Android默认使用uiautomator2，iOS默认使用XCUTest
    # 'app': r'd:\apk\bili.apk',   # apk地址，需要安装的app包
    # 'dontStopAppOnReset': True,   # 首次启动时，不停止app（可以调试或运行时提升运行速度）
    # 'skipDeviceInitialization': True  # 跳过安装、权限设置等操作（可以调试或运行时提升运行速度）
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(5)
