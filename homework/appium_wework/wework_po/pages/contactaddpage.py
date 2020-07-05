from appium.webdriver.common.mobileby import MobileBy

from homework.appium_wework.wework_po.pages.basepage import Base


class ContactAddPage(Base):
    #姓名
    _ele_name = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/b5t"]/*[@text="必填"]')
    #性别
    _ele_sex = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/csp"]//*[@text="男"]')
    _ele_sex_male = (MobileBy.XPATH,'//*[@text="男"]')
    _ele_sex_female = (MobileBy.XPATH,'//*[@text="女"]')
    #手机号
    _ele_phone = (MobileBy.XPATH,'//*[@text="手机号"]')
    #邮箱
    _ele_mailbox = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/b5t"]/*[@text="选填"]')
    #地址
    _ele_address_click = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/hd"]//*[@text="选填"]')
    _ele_address_input = (MobileBy.XPATH,'//android.widget.EditText[contains(@text,"请输入公司地址")]')
    _ele_address_choose = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/fs4"][1]')
    _ele_address_confirm = (MobileBy.XPATH,'//*[@text="确定"]')
    #身份
    _ele_identity = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/bk_"]//*[@text="普通成员"]')
    _ele_identity_common = (MobileBy.XPATH,'//*[@text="普通成员"]')
    _ele_identity_superior = (MobileBy.XPATH,'//*[@text="上级"]')
    #保存
    _ele_save = (MobileBy.XPATH,'//*[@text="保存"]')

    def edit_username(self,name):
        self.find_and_sendkeys(self._ele_name, f"{name}")
        return self

    def edit_sex(self,sex):
        self.find_and_click(self._ele_sex)
        if sex == '男':
            self.find_and_click(self._ele_sex_male)
        else:
            self.find_and_click(self._ele_sex_female)
        return self

    def edit_phone(self,phone):
        self.find_and_sendkeys(self._ele_phone, f"{phone}")
        return self

    def edit_mailbox(self,mailbox):
        self.find_and_sendkeys(self._ele_mailbox,f"{mailbox}")
        return self

    def edit_address(self,address):
        self.find_and_click(self._ele_address_click)
        self.find_and_sendkeys(self._ele_address_input, f"{address}")
        self.find_and_click(self._ele_address_choose)
        self.find_and_click(self._ele_address_confirm)
        return self

    def edit_identity(self,identity):
        self.find_and_click(self._ele_identity)
        if identity == "普通成员":
            self.find_and_click(self._ele_identity_common)
        else:
            self.find_and_click(self._ele_identity_superior)
        return self


    def click_save(self):
        self.find_and_click(self._ele_save)
        from homework.appium_wework.wework_po.pages.memberinvitepage import MemberInvitePage
        return MemberInvitePage(self.driver)


