from time import sleep

from selenium.webdriver.common.by import By

from homework.pageobject.pages.base_page import Base

class AddrbookPage(Base):


    def get_member_list(self):
        self._driver.refresh()
        #获取人员列表中的所有姓名
        getlist_elements = self._finds((By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)'))
        print(len(getlist_elements))
        memlist = []
        for i in range(len(getlist_elements)):
            memlist.append(getlist_elements[i].text)
        return memlist


    def add_member(self):
        #添加成员操作
        #查找添加成员按钮，找到两个
        sleep(3)
        addmem_elements = self._finds((By.CSS_SELECTOR,'.qui_btn.ww_btn.js_add_member'))
        #对第一个进行点击操作
        addmem_elements[1].click()
        #录入人员姓名
        self._find((By.ID,"username")).send_keys("李二三")
        #录入人员帐号
        self._find((By.ID,"memberAdd_acctid")).send_keys("lier3")
        #录入手机号
        self._find((By.ID,"memberAdd_phone")).send_keys("13678107970")
        #获取保存按钮
        save_elements = self._finds((By.CSS_SELECTOR,'.qui_btn.ww_btn.js_btn_save'))
        save_elements[0].click()

    def delete_member(self):
        sleep(2)
        #点击第一行数据的checkbox
        self._find((By.CSS_SELECTOR,'#member_list tr:nth-child(1) input')).click()
        #获取删除按钮
        delete_elements = self._finds((By.CSS_SELECTOR,'.qui_btn.ww_btn.js_delete'))
        #点击删除
        delete_elements[0].click()
        #弹框中提示是否确定删除成员
        #获取确定按钮
        confirm_elements = self._finds((By.CSS_SELECTOR,'.qui_btn.ww_btn.ww_btn_Blue'))
        #点击确定
        confirm_elements[1].click()


#调试模块时用的
if __name__ == '__main__':
    addrbook = AddrbookPage()
    a = addrbook.get_member_list()
    print(a)
