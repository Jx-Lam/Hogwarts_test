from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from web.po_test.web_page.contact_page import ContactPage


class HomePage:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)

    def goto_memberedit(self):
        self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        # 点击添加成员按钮
        locator_add = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        element: WebElement = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator_add))
        element.click()

        return ContactPage(self.driver)
