from time import sleep

import yaml
from appium import webdriver
import appium
import pytest

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
        self.driver.find_element_by_xpath(f'//*[@resource-id="com.tencent.wework:id/dz9"]//*[@text="{name}"]').click()
        #进入个人信息
        self.driver.find_element_by_xpath('//*[@text="个人信息"]/../../../../..//*[@class="android.widget.RelativeLayout"]').click()
        #编辑成员
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        #删除成员
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        #确定删除
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        #强等3秒人员从通讯录去除
        sleep(3)
        # 获取通讯录所有人员
        members = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.wework:id/dec"]//*[@class="android.widget.TextView"]')
        #要删除的人员对象
        mem_list = [member.get_attribute("text") for member in members]
        print(mem_list)
        assert name not in mem_list

