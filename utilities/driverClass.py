from appium import webdriver


class Driver:
    @staticmethod
    def get_driver_method():
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "11"
        desired_caps["deviceName"] = "Xiaomi Redmi Note 8 Pro"
        desired_caps["automationName"] = "UiAutomator2"
        desired_caps["appPackage"] = "com.code2lead.kwad"
        desired_caps["appActivity"] = "com.code2lead.kwad.MainActivity"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver
