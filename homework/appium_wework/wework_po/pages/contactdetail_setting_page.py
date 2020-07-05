from appium.webdriver.common.mobileby import MobileBy

from homework.appium_wework.wework_po.pages.basepage import Base
from homework.appium_wework.wework_po.pages.editmemberpage import EditMemberPage


class ContactDetailSettingPage(Base):
    #编辑成员
    _ele_editmember = (MobileBy.XPATH,'//*[@text="编辑成员"]')
    def goto_editmember(self):
        self.find_and_click(self._ele_editmember)
        return EditMemberPage(self.driver)