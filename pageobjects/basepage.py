from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    scroll_down_script = "window.scrollBy(0, 500);"
    scroll_mid_script = "window.scrollBy(0,400);"

    def __init__(self, driver):
        self.driver = driver

    def clear_browser_cache(self):
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
        self.driver.execute_script("window.location.reload();")

    def finding_element(self, locator):
        return self.driver.find_element(*locator)

    def finding_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_by_finding_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_to_click(self):
        waiting = WebDriverWait(self.driver, 20)
        return waiting

    def click_when_clickable(self, args):
        wait = self.wait_to_click()
        wait.until(EC.element_to_be_clickable(args)).click()

    def click_when_visibility(self, args):
        wait = self.wait_to_click()
        wait.until(EC.visibility_of_element_located(args)).click()

    def send_keys_when_clickable(self, args, values):
        wait = self.wait_to_click()
        wait.until(EC.element_to_be_clickable(args)).send_keys(values)

    def send_when_visibility(self, args, values):
        wait = self.wait_to_click()
        wait.until(EC.visibility_of_element_located(args)).send_keys(values)

    def get_title(self, title):
        wait = self.wait_to_click()
        wait.until(EC.title_is(title))
        return self.driver.title

    """Action Chains methods are described below"""

    def action_chains_methods(self):
        action = ActionChains(self.driver)
        return action

    def mouse_over_action_on_element(self, args):
        locator = self.finding_element(args)
        action = self.action_chains_methods()
        action.move_to_element(locator).perform()

    def mouse_over_click_on_element(self, args):
        locator = self.finding_element(args)
        action = self.action_chains_methods()
        action.move_to_element(locator).click().perform()

    """"Javascript executor methods are written below"""

    def java_script_scroll_down(self):
        self.driver.execute_script(self.scroll_down_script)

    def java_script_scroll_mid(self):
        self.driver.execute(self.scroll_mid_script)

    """"Search by search field"""
    def set_items_by_search_(self,locator,value):
        element = self.finding_element(locator)
        element.sendkeys(value)

    def get_seacrh_items_by_click(self,locator):
        search= self.finding_element(locator)
        self.click_when_clickable(search)
