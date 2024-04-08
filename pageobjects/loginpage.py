

from selenium.webdriver.common.by import By

from pageobjects.basepage import BasePage


class LoginPage(BasePage):
    MyAccount_field = (By.XPATH, "//span[text()='My Account']")
    Login_field = (By.LINK_TEXT, "Login")
    username_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button_field = (By.XPATH, "//input[@value='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_MyAccount_page(self):
        self.click_when_clickable(self.MyAccount_field)

    def get_into_login_page(self):
        self.click_when_visibility(self.Login_field)

    def set_username(self, username):
        self.click_when_clickable(self.username_field)
        self.send_when_visibility(self.username_field, username)

    def set_password(self, password):
        self.click_when_clickable(self.password_field)
        self.send_when_visibility(self.password_field, password)

    def get_login_button(self):
        self.java_script_scroll_down()
        self.click_when_visibility(self.login_button_field)

    def get_login_successfully(self, username, password):
        self.get_MyAccount_page()
        self.get_into_login_page()
        self.set_username(username)
        self.set_password(password)
        self.get_login_button()

    def get_cleared_by_browser_cache(self):
        self.clear_browser_cache()

