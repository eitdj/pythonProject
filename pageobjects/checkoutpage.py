from selenium.webdriver.common.by import By

from pageobjects.basepage import BasePage


class CheckOutPage(BasePage):
    cart_field = (By.ID, "cart-total")
    cart_popup_field = (By.CLASS_NAME, "dropdown-menu pull-right")
    view_cart_field = (By.XPATH, "//p[@class='text-right']//a[1]")
    view_checkout_field = (By.XPATH, "//p[@class='text-right']//a[2]")
    firstname_field = (By.NAME, "firstname")
    lastname_field = (By.NAME, "lastname")
    address_field = (By.NAME, "address_1")
    city_field = (By.NAME, "city")
    postcode_field = (By.NAME, "postcode")
    country_field = (By.TAG_NAME, "select")
    region_field = (By.NAME, "zone_id")
    continue_button_on_billing = (By.XPATH, "input[value='Continue']")
    continue_button_payement_field = (By.XPATH, "//input[@value='Continue']")
    terms_condition_field = (By.XPATH, "(//div[@class='pull-right'])[2]/child::input[1]")
    continue_button_terms_condition_field = (By.XPATH, "(//input[@value='Continue'])[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_checkout_macbook(self):
        self.click_when_visibility(self.cart_field)

    def get_checkout_macbook_table(self):
        self.click_when_visibility(self.cart_popup_field)

    def get_view_cart_table(self):
        self.click_when_clickable(self.view_cart_field)

    def get_checkout_tab(self):
        self.click_when_visibility(self.view_checkout_field)

    def set_billing_Details_in_checkout(self):
        self.send_when_visibility(self.firstname_field, "dj")
        self.send_when_visibility(self.lastname_field, "rj")
        self.send_when_visibility(self.address_field, "banglore")
        self.send_when_visibility(self.city_field, "banglalore")
        self.send_when_visibility(self.postcode_field, 577301)

    def select_country_dropdown(self):
        countries = self.finding_elements(self.country_field)
        for country in countries:
            country_text = country.text
            if country_text == "India":
                country.click()
                break

    def select_region_dropdown(self):
        regions = self.click_when_visibility(self.region_field)
        for region in regions:
            regions_text = regions.text
            if regions_text == "kent":
                region.click()
                break

    def get_button_payment_address(self):
        self.click_when_visibility(self.continue_button_on_billing)

    def get_continue_payment_with_existing_value(self):
        self.click_when_visibility(self.continue_button_payement_field)

    def set_confirm_terms_and_conditions(self):
        self.java_script_scroll_down()
        self.click_when_visibility(self.terms_condition_field)

    def get_confirm_terms_and_conditions(self):
        self.click_when_visibility(self.continue_button_terms_condition_field)

    def checkout_new_address(self):
        self.set_billing_Details_in_checkout()
        self.select_country_dropdown()
        self.select_region_dropdown()
        self.get_button_payment_address()
        self.get_continue_payment_with_existing_value()
        self.set_confirm_terms_and_conditions()
        self.get_confirm_terms_and_conditions()

    def checkout_existing_address(self):
        self.get_button_payment_address()
        self.get_continue_payment_with_existing_value()
        self.set_confirm_terms_and_conditions()
        self.get_confirm_terms_and_conditions()

