from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ContactPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def member_edit(self, username, account, phone):
        # 添加联系人信息
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(account)
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        locator_save = (By.CSS_SELECTOR, '#js_tips')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator_save))

    def get_member(self):
        title_list = []
        contact_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        for contact in contact_list:
            title_list.append(contact.get_attribute('title'))
        print(title_list)
        return title_list
