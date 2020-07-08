import pytest
import yaml

from homework.appium_wework.wework_po.pages.app import App


class TestWeWork:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()


    def teardown_class(self):
        self.app.close()

    @pytest.mark.parametrize(['name','sex','phone','mailbox','address','identity'],
                             yaml.safe_load(open("../datas/data.yaml", encoding='utf-8'))['add'])
    def test_add_contact(self,name,sex,phone,mailbox,address,identity):
        toast = self.main.goto_addresslist().goto_memberinvite()\
                        .goto_contactadd().edit_username(name).edit_sex(sex).edit_phone(phone)\
                        .edit_mailbox(mailbox).edit_address(address).edit_identity(identity).click_save().get_toast()

        assert toast == '添加成功'
        self.main.back()

    @pytest.mark.parametrize(['name1','name2'], yaml.safe_load(open("../datas/data.yaml", encoding='utf-8'))['del'])
    def test_del_contact(self,name1,name2):
        result = self.main.goto_addresslist().goto_contactdetail_briefinfo(name1)\
            .goto_contactdetail_setting().goto_editmember().del_member().del_confirm().member_disappear(name2)

        assert result == True
