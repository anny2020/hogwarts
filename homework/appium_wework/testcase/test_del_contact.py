from time import sleep

import yaml
from appium import webdriver
import appium
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from homework.appium_wework.testcase.base_test import BaseTest


class TestDelContact(BaseTest):
    @classmethod
    def setup_class(cls):
        BaseTest().setup_class()

    @classmethod
    def teardown_class(cls):
        BaseTest().teardown_class()

    def setup(self):
        BaseTest().setup()

    def teardown(self):
        BaseTest().teardown()

    @pytest.mark.parametrize("name",yaml.safe_load(open("data.yaml",encoding='utf-8'))['del'])
    def test_del_contact(self,name):
        # 在登录后首页点击“通讯录”
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        #找到要删除的人员
        # self.driver.find_element_by_xpath(f'//*[@resource-id="com.tencent.wework:id/dz9"]//*[@text="{name}"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).'
                                                        f'instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));').click()
        #进入个人信息
        self.driver.find_element_by_xpath('//*[@text="个人信息"]/../../../../..//*[@class="android.widget.RelativeLayout"]').click()
        #编辑成员
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        #删除成员
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        #确定删除
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        assert WebDriverWait(self.driver,10).until_not(lambda x:x.find_element_by_xpath(f"//*[@text='{name}']")) == True

