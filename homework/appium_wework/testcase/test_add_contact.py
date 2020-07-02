from time import sleep

import yaml
from appium import webdriver
import pytest
from selenium.webdriver.common.by import By

from homework.appium_wework.testcase.base_test import BaseTest


class TestAddContact(BaseTest):

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

    @pytest.mark.parametrize(["name","sex","phone","mailbox","address","sf"],yaml.safe_load(open("data.yaml",encoding='utf-8'))['add'])
    def test_add_contact(self,name,sex,phone,mailbox,address,sf):
        #在登录后首页点击“通讯录”
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/dyu"]//*[@text="通讯录"]').click()
        #在通讯录页面点击“添加成员”
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        #在添加成员页面点击“手动输入添加”
        self.driver.find_element_by_id("com.tencent.wework:id/cch").click()
        #添加成员信息
        #姓名
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/b5t"]/*[@text="必填"]').send_keys(f"{name}")
        #性别
        self.driver.find_element_by_id("com.tencent.wework:id/axu").click()
        if sex == '男':
            self.driver.find_element_by_xpath('//*[@text="男"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="女"]').click()
        #手机号
        self.driver.find_element_by_id("com.tencent.wework:id/f1e").send_keys(f"{phone}")
        #邮箱
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/b5t"]/*[@text="选填"]').send_keys(f"{mailbox}")
        #地址
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/hd"]//*[@text="选填"]').click()
        self.driver.find_element_by_id("com.tencent.wework:id/he").send_keys(f"{address}")
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/fs4"][1]').click()
        self.driver.find_element_by_id("com.tencent.wework:id/h9w").click()
        #设置部门 使用默认
        #身份
        self.driver.find_element_by_id("com.tencent.wework:id/bk_").click()
        if sf == "普通成员":
            self.driver.find_element_by_xpath('//*[@text="普通成员"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="上级"]').click()
        self.driver.find_element_by_id("com.tencent.wework:id/h9w").click()
        ele_toast = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]')
        print(ele_toast.text)
        #添加成功后，返回通讯录页
        self.driver.find_element_by_id("com.tencent.wework:id/h9e").click()
        #获取通讯录所有人员
        members = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.wework:id/dec"]//*[@class="android.widget.TextView"]')
        print(len(members))
        mem_list = []
        for i in range(len(members) - 1):
            mem_list.append(members[i].get_attribute("text"))
        print(mem_list)
        assert name in mem_list




