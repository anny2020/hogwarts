'''
需求：完成以下测试用例：
1.删除成员
2.导入通讯录
思路：
1.通过首页-->点击通讯录导航标签-->进入通讯录页面，获取页面人员列表，如果列表不为空，选择列表中第一个进行删除操作。
2.通过首页-->导入通讯录-->进入通讯录页面，进行导入操作。

'''
from time import sleep

from selenium.webdriver.common.by import By

from homework.pageobject.pages.addrbook_page import AddrbookPage
from homework.pageobject.pages.base_page import Base
from homework.pageobject.pages.import_page import ImportPage


class MainPage(Base):
    baseurl = "https://work.weixin.qq.com/wework_admin/frame#index"

    #从导航标签进入通讯录页面
    def entry_addrbook(self):
        self.find((By.ID,"menu_contacts")).click()
        return AddrbookPage(self.driver)

    #导入通讯录
    def import_addrbook(self):
        self.find((By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)")).click()
        return ImportPage(self.driver)



