from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    #初始化Url为空
    baseurl = ""

    def __init__(self,driver:webdriver=None):
        #使用debug的方式登录
        option = Options()
        #启动Ip和端口
        option.debugger_address="localhost:9222"

        #判断driver为空时，就实例化driver
        if driver is None:
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver
        #当地址有值时，打开网址
        if self.baseurl != "":
            self.driver.get(self.baseurl)

    #封装了查找单个元素的方法，并加入了显示等待
    def find(self,*by):
        return WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(*by))

    #封闭了查找多个元素的方法，并加入了显示等待
    def finds(self,*by):
        return WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(*by))


