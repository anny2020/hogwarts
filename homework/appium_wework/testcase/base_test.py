from appium import webdriver


class BaseTest:
    @classmethod
    def setup_class(cls):
        desire_cap = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": True,
            # "dontStopAppReset": True,
            "skipDeviceInitialization": True,
            # "automationName": "uiautomator2"
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        cls.driver.implicitly_wait(25)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup(self):
        # 登录帐号
        self.driver.find_element_by_id("com.tencent.wework:id/a0t").click()
        # 选择公司
        self.driver.find_element_by_xpath('//*[@text="anny"]').click()
        # 进入企业
        self.driver.find_element_by_id("com.tencent.wework:id/c3w").click()

    def teardown(self):
        # 退出帐号
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/gud"]//*[@text="我"]').click()
        self.driver.find_element_by_id("com.tencent.wework:id/g7k").click()
        self.driver.find_element_by_id("com.tencent.wework:id/g7o").click()
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.tencent.wework:id/bce"]//*[@text="退出当前帐号"]').click()
        self.driver.find_element_by_id("com.tencent.wework:id/bci").click()