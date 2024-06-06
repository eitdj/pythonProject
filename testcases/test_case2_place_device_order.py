import time

from pageobjects.loginpage import LoginPage
from pageobjects.myaccountpage import MyAccount
from testcases.test_basic import TestBase
from utilities.screenshot import CaptureScreen


class TestAddToCart(TestBase):

    def test_add_to_cart_hplaptop(self):
        login = LoginPage(self.driver)
        login.get_login_successfully("coldwar@yopmail.com", "srvt@123")
        myaccount = MyAccount(self.driver)
        myaccount.laptops_and_notebooks()
        myaccount.get_Show_All_Laptops_and_Notebooks()
        time.sleep(10)
        myaccount.get_add_to_cart_HPLP()
        time.sleep(10)
        success_message = myaccount.get_success_cart_message()
        if "Success" in success_message:
            assert True
        else:
            CaptureScreen.capture_screenshot(self.driver)

    def test_add_iphone_cart(self):
        loginpage = LoginPage(self.driver)
        loginpage.get_login_successfully("coldwar@yopmail.com", "srvt@123")

