# -*- coding: utf-8 -*-
import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestReuse:
    # 复用浏览器
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()

    def cleardown_method(self):
        self.driver.quit()

    def test_get(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#inde")

    # 获取当前打开页面的cookie
    def test_get_cookie(self):
        self.cookies = self.driver.get_cookies()
        print(self.cookies)

    def test_store_cookie(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'A4iv6j5Kvj2gLanbBr6okKQkBfXZI5Y8VTIx0eU6FoLFOfNzvzSb9g6dQzBhrL7T_7atK_kHSHR21AonT7xwai5BcWNT_oD7Nc1L8FOiMG2pbD1Z4hTyITTD7CFO0cZ2KqeBPDsOcC4my5qb4L8cCJ28BwQ9SDMe_VR5PGCLlxKMUWun1rVZ5YyYjQ25_bEQHbfwjleUKEjuIYST7J2Y_gD9D4HgQTcNx-Qw8ZWTz6bmErU3MclUGVH4q-2tbMWbz7JPw-ukA2ZCvetciJrlXg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850347065656'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325129170337'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'HY_km99DX5O1ne3GQFfPeuuKegaa99J4yS3Cb-bnJ8QOue1kTD9wNMX8CL-_ozpS'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a775985'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '4001074237947895'},
            {'domain': '.qq.com', 'expiry': 1666690459, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1656413748.1603589303'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635125286, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850347065656'},
            {'domain': '.qq.com', 'expiry': 1626059818, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/',
             'secure': False, 'value': '1594523819556'},
            {'domain': '.qq.com', 'expiry': 1626059818, 'httpOnly': False, 'name': 'sd_userid', 'path': '/',
             'secure': False, 'value': '16811594523819556'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '7348162572'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635125395, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603589302'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606210468, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'b44ace229b06983872e63bfd99c3c5058ccd31cd53bb63eed788095c2c7a3382'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'FbRJ2BrsRT'},
            {'domain': '.qq.com', 'expiry': 1603704859, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.474307113.1603589303'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603620822, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '7jm2a87'},
            {'domain': '.qq.com', 'expiry': 1603618519, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '7158510592'}]
        db = shelve.open("cookies")  # 打开cookies数据库
        db['cookie'] = cookies
        db.close()
