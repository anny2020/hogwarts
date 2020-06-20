import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.driver.maximize_window()
    #只要执行一次此方法来获取cookies后，以后可以只使用test_login来直接登陆就可以跳过扫码了
    def test_cookie(self):
        sleep(10)
        cookies = self.driver.get_cookies()
        with open("data.json","w") as f:
            json.dump(cookies,f)

    def test_login(self):
        cookies = json.load(open("data.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            result = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,"menu_index")))
            print(result.text)
            if result.text == "首页":
                break
        #把查找元素改成显示等待
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                '.index_service_cnt_itemWrap:nth-child(2)')))
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()

        #对于input标签的文件上传，要用Input标签来定位
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR,'#js_upload_file_input')))
        self.driver.find_element(By.CSS_SELECTOR,'#js_upload_file_input').send_keys("E:/hogwarts/test_selenium/test.xlsx")
        #断言文件名是上传的文件名
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".import_settingStage_upload_fileName")))
        filename = self.driver.find_element(By.CSS_SELECTOR, ".import_settingStage_upload_fileName").text
        assert filename == "test.xlsx"



    def teardown(self):
        self.driver.quit()

