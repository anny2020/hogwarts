from appium.webdriver.common.mobileby import MobileBy

from homework.appium_wework.wework_po.pages.basepage import Base


class MemberInvitePage(Base):
    #手动输入添加
    _ele_contactadd = (MobileBy.XPATH,'//*[@text="手动输入添加"]')

    #进入到手动输入添加
    def goto_contactadd(self):
        self.find_and_click(self._ele_contactadd)
        from homework.appium_wework.wework_po.pages.contactaddpage import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        toast = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        return toast
