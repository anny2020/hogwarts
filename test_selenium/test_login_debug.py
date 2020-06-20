from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

class TestLogin:
    def test_debug_login(self):
        #option相当于工具
        option = Options()
        #指定了一个调试地址
        option.debugger_address="localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts/import_auto/1688853782840223")

