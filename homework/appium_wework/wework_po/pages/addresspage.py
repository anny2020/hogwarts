from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from homework.appium_wework.wework_po.pages.basepage import Base
from homework.appium_wework.wework_po.pages.contactdetail_briefinfo_page import ContactDetailBriefInfoPage
from homework.appium_wework.wework_po.pages.memberinvitepage import MemberInvitePage


class AddressPage(Base):


    #进入添加成员
    def goto_memberinvite(self):
        self.find_by_scroll("添加成员")
        return MemberInvitePage(self.driver)

    #进入到个人信息
    def goto_contactdetail_briefinfo(self,name):
        self.find_by_scroll(name)
        return ContactDetailBriefInfoPage(self.driver)


    def member_disappear(self,name):
        return WebDriverWait(self.driver,15).until_not(lambda x:x.find_element_by_xpath(f"//*[@text='{name}']"))
