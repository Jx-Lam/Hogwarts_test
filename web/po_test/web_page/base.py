from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化  chrome --remote-debugging-port=9222
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(5)
        else:
            # 对页面进行调整
            self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # # 封装一个函数，用来判断属性值是否存在
    # def isElementPresent(self, by, value):
    #     """
    #     用来判断元素标签是否存在，
    #     """
    #     try:
    #         element = self.driver.find_element(by=by, value=value)
    #     # 原文是except NoSuchElementException, e:
    #     except NoSuchElementException as e:
    #         # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
    #         return False
    #     else:
    #         # 没有发生异常，表示在页面中找到了该元素，返回True
    #         return True
