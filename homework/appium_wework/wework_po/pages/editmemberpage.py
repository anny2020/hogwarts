from appium.webdriver.common.mobileby import MobileBy

from homework.appium_wework.wework_po.pages.basepage import Base


class EditMemberPage(Base):
    # 删除成员
    _ele_delmember = (MobileBy.XPATH,'//*[@text="删除成员"]')
    #确定删除
    _ele_confirmdel = (MobileBy.XPATH,'//*[@text="确定"]')
    #取消删除
    _ele_canceldel = (MobileBy.XPATH,'//*[@text="取消"]')
    def del_member(self):
        self.find_and_click(self._ele_delmember)
        return self

    def del_confirm(self):
        self.find_and_click(self._ele_confirmdel)
        from homework.appium_wework.wework_po.pages.addresspage import AddressPage
        return AddressPage(self.driver)

    def del_cancel(self):
        self.find_and_click(self._ele_canceldel)
        return self
