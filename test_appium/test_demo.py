# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import logging
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["udid"] = "HFK9K19430909096"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存，启动app
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):

        el1 = self.driver.find_element_by_id("com.tencent.wework:id/a41")
        el1.click()
        sleep(2)
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/blx")
        el2.click()
        sleep(2)
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/fop")
        el3.click()

        sleep(2)
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/fow")
        el4.send_keys("13631220216")
        sleep(2)
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/di")
        el5.click()
        desc = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b1h").text
        assert desc == "没有获取到验证码？"

    # def test_daka(self):
    #     self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
    #     self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
    #                              'new UiScrollable(new UiSelector().'
    #                              'scrollable(true).instance(0)).'
    #                              'scrollIntoView(new UiSelector().'
    #                              'text("打卡").instance(0));').click()
    #     self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
    #     self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
    #     r = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/mn").text
    #     assert r == "外出打卡成功"
    #
    # def test_add_member(self):
    #     name = 'zhangsan2'
    #     gender = '男'
    #     phonenum = '18200000002'
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
    #     # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
    #     self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
    #                              'new UiScrollable(new UiSelector().'
    #                              'scrollable(true).instance(0)).'
    #                              'scrollIntoView(new UiSelector().'
    #                              'text("添加成员").instance(0));').click()
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
    #     self.driver.find_element(MobileBy.XPATH ,"//*[@text='男']").click()
    #     if gender == '女':
    #         self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
    #     else:
    #         self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eq7").send_keys(phonenum)
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
    #     ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
    #     assert "添加成功" == ele





