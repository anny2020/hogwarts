from appium.webdriver.common.mobileby import MobileBy

from homework.appium_wework.wework_po.pages.addresspage import AddressPage
from homework.appium_wework.wework_po.pages.basepage import Base
from homework.appium_wework.wework_po.pages.workbenchpage import WorkBenchPage


class MainPage(Base):
    #通讯录
    _ele_contact = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/dyu"]//*[@text="通讯录"]')

    #工作台
    _ele_workbench = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/dyu"]//*[@text="工作台"]')

    #进入到通讯录
    def goto_addresslist(self):
        self.find_and_click(self._ele_contact)
        return AddressPage(self.driver)
    #进入消息
    def goto_message(self):
        return self
    #进入工作台 有空会继续补充
    # def goto_workbench(self):
    #     self.find_and_click(self._ele_workbench)
    #     return WorkBenchPage(self.driver)
    #进入我的
    def goto_me(self):
        pass