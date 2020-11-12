from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.po_test.web_page.base import BasePage


class ContactPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def member_edit(self, username, account, phone):
        # 添加联系人信息
        self.find(By.CSS_SELECTOR, '#username').send_keys(username)
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(account)
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        locator_save = (By.CSS_SELECTOR, '#js_tips')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator_save))

    def get_member(self, value):
        title_list = []
        total_list = []

        while True:
            # 获取当前页的联系方式
            contact_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
            for contact in contact_list:  # 另外一种写法：
                title_list.append(contact.get_attribute(
                    'title'))  # titlelist = [element.get_attribute("title") for element in contactlist]
            # 将当前页面的联系方式，添加至总通讯录中
            total_list = total_list + title_list

            print(f"total_list:{total_list}")
            print(f"title_list:{title_list}")

            if value in total_list:
                return True

            try:
                # 查询手机号不在当前联系方式页面中，则点击下一页
                page: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
                current_num, total_num = page.split('/', 1)
                if current_num == total_num:
                    # 查询所有通讯页，仍未查到该用户
                    return False
                else:
                    self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
            except:
                return False

        print(title_list)
        return total_list
