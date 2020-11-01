# 1.导入依赖
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

# 2.capabilities 设置
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '6',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称
    'appActivity': '.ui.splash.SplashActivity',  # 启动Activity名称，如被测的页面
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True，是否需要输入非英文之外的语言
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 是否在测试前后重置相关环境，true则为不重置，如登录信息、权限设置。fullReset
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'  # 引擎，Android默认使用uiautomator2，iOS默认使用XCUTest
    # 'app': r'd:\apk\bili.apk',   # apk地址，需要安装的app包
    # 'dontStopAppOnReset': True,   # 首次启动时，不停止app（可以调试或运行时提升运行速度）
    # 'skipDeviceInitialization': True  # 跳过安装、权限设置等操作（可以调试或运行时提升运行速度）
}

# 3.连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 4.隐式等待，设置缺省等待时间
driver.implicitly_wait(5)

# 5.元素定位与操作 find + action
# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements_by_id("text3")
if iknow:
    iknow.click()

# 根据id定位搜索位置框，点击
driver.find_element_by_id("expand_search").click()

# 根据id定位搜索输入框，点击
sbox = driver.find_element_by_id('search_src_text')
sbox.send_keys('白月黑羽')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
eles = driver.find_elements_by_id("title")

# 6.断言
for ele in eles:
    # 打印标题
    print(ele.text)

input('**** Press to quit..')
driver.quit()
