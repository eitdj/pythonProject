from selenium.webdriver.common.by import By

from pageobjects.basepage import BasePage


class MyAccount(BasePage):
    laptop_notebooks_field = (By.LINK_TEXT, "Laptops & Notebooks")
    Show_All_Laptops_and_Notebooks_filed = (By.LINK_TEXT, "Show All Laptops & Notebooks")
    hplp_3085_field = (By.XPATH, "(//span[text()='Add to Cart'])[2]")
    success_cart_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    search_tab_input_field = (By.XPATH, "//div[@id = 'search']")
    search_button = (By.XPATH, "//div[@id = 'search']/child::span/button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_iphone_by_search(self):
        self.set_items_by_search_(self.search_tab_input_field)
        self.get_seacrh_items_by_click(self.search_button)
        self.scroll_down_script()
        self.scroll_mid_script()




    def laptops_and_notebooks(self):
        self.click_when_visibility(self.laptop_notebooks_field)

    def get_Show_All_Laptops_and_Notebooks(self):
        self.click_when_visibility(self.Show_All_Laptops_and_Notebooks_filed)

    def get_add_to_cart_HPLP(self):
        self.java_script_scroll_down()
        self.click_when_visibility(self.hplp_3085_field)

    def laptops_and_notebooks_mouse(self):
        self.mouse_over_click_on_element(self.laptop_notebooks_field)

    def get_Show_All_Laptops_and_Notebooks_mouse(self):
        self.mouse_over_click_on_element(self.Show_All_Laptops_and_Notebooks_filed)
        self.java_script_scroll_down()

    def get_success_cart_message(self):
        message = self.finding_element(self.success_cart_message)
        return message.text

    def get_in_my_account_page(self):
        self.laptops_and_notebooks()
        self.get_Show_All_Laptops_and_Notebooks()

    def get_in_my_account_page_validation(self):
        self.laptops_and_notebooks()
        self.get_Show_All_Laptops_and_Notebooks()
        self.get_add_to_cart_HPLP()

