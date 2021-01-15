import allure, time
from selenium import webdriver


class Test002:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        time.sleep(2)

    @allure.step("输入用户名")
    def input_name(self, name):
        pass

    @allure.step("输入密码")
    def input_password(self, password):
        pass

    @allure.step("登录步骤")
    def test_login(self):
        self.input_name("李白")
        self.input_password("123456")
        allure.attach("这是标题", "标题", allure.attachment_type.TEXT)

        allure.attach(self.driver.get_screenshot_as_png(), "图片标题", allure.attachment_type.PNG)

        self.driver.quit()
