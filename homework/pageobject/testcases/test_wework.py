from time import sleep

import pytest

from homework.pageobject.pages.main_page import MainPage


class TestWework:
    def setup(self):
        #对主页对象进行实例化
        self.mainpage = MainPage()


    #添加人员的case
    def test_addmem(self):
        #从主页进入通讯录添加人员操作
        self.mainpage.entry_addrbook().add_member()
        #从主页进入通讯录获取人员列表
        sleep(3)
        memlist = self.mainpage.entry_addrbook().get_member_list()
        #验证添加的人员“李书”在通讯录列表中
        assert "李二三" in memlist

    #删除人员的case
    def test_delmem(self):
        #从主页通讯录进入通讯录页面删除人员操作
        self.mainpage.entry_addrbook().delete_member()
        #从主页通讯录进入获取人员最新列表
        memlist = self.mainpage.entry_addrbook().get_member_list()
        #验证删除的人员不在列表中
        assert "李二三" not in memlist

    def test_importaddr(self):
        #从主页导入通讯录进入录入页面
        self.mainpage.import_addrbook().import_member()
        #从主页通讯录进入获取人员列表
        memlist = self.mainpage.entry_addrbook().get_member_list()
        #验证录入的人员在列表中
        assert "张牛" in memlist









