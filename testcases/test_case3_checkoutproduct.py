import time

from pageobjects.checkoutpage import CheckOutPage
from pageobjects.loginpage import LoginPage
from pageobjects.myaccountpage import MyAccount
from testcases.test_basic import TestBase


class TestCheckoutPage(TestBase):
    def test_checkout_page_validation(self):

        login = LoginPage(self.driver)
        login.get_login_successfully("eit@yopmai.com", "srvt@123")
        myaccount = MyAccount(self.driver)
        myaccount.get_in_my_account_page_validation()
        checkout = CheckOutPage(self.driver)
        checkout.get_checkout_macbook()
        checkout.get_checkout_tab()

        checkout.get_continue_payment_with_existing_value()
        time.sleep(5)
        checkout.set_confirm_terms_and_conditions()
        checkout.get_confirm_terms_and_conditions()
        # checkout.set_billing_Details_in_checkout()
        # checkout.select_country_dropdown()
        # checkout.select_region_dropdown()
        # checkout.get_button_payment_address()
        time.sleep(5)