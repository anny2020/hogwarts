import os

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from homework.appium_wework.wework_po.pages.basepage import Base
from homework.appium_wework.wework_po.pages.mainpage import MainPage


class App(Base):
    #启动app
    def start(self):
        if self.driver is None:
            desire_cap = {
                "platformName": "Android",
                "platformVersion": "6.0.1",
                # "deviceName": "127.0.0.1:7555",
                "udid": os.getenv('udid',None),
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": True,
                "skipDeviceInitialization": True,
                "unicodeKeyBoard": True,
                "resetKeyBoard": True
            }
            # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            self.driver = webdriver.Remote("http://192.168.0.101:4444/wd/hub", desire_cap)

        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(25)
        return self


    def close(self):
        self.driver.quit()

    def main(self):
        return MainPage(self.driver)