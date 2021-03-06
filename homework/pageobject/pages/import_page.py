from time import sleep

from selenium.webdriver.common.by import By

from homework.pageobject.pages.base_page import Base


class ImportPage(Base):


    def import_member(self):
        sleep(3)
        #上传文件导入
        self._find((By.ID,'js_upload_file_input')).send_keys(
            "E:/hogwarts/homework/pageobject/pages/addrbookfile.xlsx")
        #点击确认导入按钮
        self._find((By.ID,'submit_csv')).click()
        #前往查看按钮
        self._find((By.ID,'reloadContact')).click()

#调试模块用的
if __name__ == '__main__':
    impo = ImportPage()
    impo.import_member()