# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class TestReuse:
    # 复用浏览器
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#inde")
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_main_add(self):
        # 添加联系人信息
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('a4')
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('13600000004')
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('13600000004')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

        # 验证添加成功
        title_list = []
        contact_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        for element in contact_list:
            title_list.append(element.get_attribute('title'))
        print(title_list)
        assert '13600000004' in title_list

    def test_menu_add(self):
        self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        # 点击添加成员按钮
        locator_add = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        element: WebElement = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator_add))
        element.click()
        # 添加联系人信息
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('a8')
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('13600000008')
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('13600000008')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        # 验证添加成功
        # sleep(10)
        locator_save = (By.CSS_SELECTOR, '#js_tips')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator_save))
        title_list = []
        contact_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        for contact in contact_list:
            title_list.append(contact.get_attribute('title'))
        print(title_list)
        assert '13600000008' in title_list
