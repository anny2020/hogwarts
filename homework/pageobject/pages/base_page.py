from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    baseurl = ""

    def __init__(self,driver:webdriver=None):
        #使用debug的方式登录
        option = Options()
        option.debugger_address="localhost:9222"

        if driver is None:
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver
        if self.baseurl != "":
            self.driver.get(self.baseurl)

    def find(self,*by):
        return WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(*by))
        # return self.driver.find_element(by,locator)

    def finds(self,*by):
        # return self.driver.find_elements(by,locator)
        return WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(*by))
        # return WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(*by))


