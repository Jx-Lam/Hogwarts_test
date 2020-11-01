# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWeiXin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        # shelve中读取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        # 添加cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            r"D:\code\project\hogwarts_test\web\address.xlsx")
        # 断言
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert filename == 'address.xlsx'
        sleep(3)
