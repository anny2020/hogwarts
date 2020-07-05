from appium.webdriver.common.mobileby import MobileBy

from homework.appium_wework.wework_po.pages.basepage import Base
from homework.appium_wework.wework_po.pages.contactdetail_setting_page import ContactDetailSettingPage


class ContactDetailBriefInfoPage(Base):
    #三个点
    _ele_membersetting = (MobileBy.XPATH,'//*[@text="个人信息"]/../../../../..//*[@class="android.widget.RelativeLayout"]')

    #点击三个点,进入个人信息
    def goto_contactdetail_setting(self):
        self.find_and_click(self._ele_membersetting)
        return ContactDetailSettingPage(self.driver)