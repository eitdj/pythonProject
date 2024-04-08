import time

from pageobjects.loginpage import LoginPage
from testcases.test_basic import TestBase
from utilities.screenshot import CaptureScreen


class TestLoginPage(TestBase):
    def test_login_with_valid_user(self):
        self.login = LoginPage(self.driver)
        time.sleep(5)
        self.login.get_MyAccount_page()
        time.sleep(5)
        self.login.get_into_login_page()
        time.sleep(5)
        self.login.set_username("coldwar@yopmail.com")
        self.login.set_password("srvt@123")
        self.login.get_login_button()
        time.sleep(6)
        account_title = self.driver.title
        if account_title == "ccount Login":
            assert True
        else:
            CaptureScreen.capture_screenshot(self.driver)
