import pytest
from selenium import webdriver

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def launch(request):
    serv = Service("C:\\Users\\EIT\\Pictures\\j\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv)
    driver.delete_all_cookies()
    driver.get("https://naveenautomationlabs.com/opencart/")

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
