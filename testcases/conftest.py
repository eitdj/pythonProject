import pytest
from selenium import webdriver

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )


@pytest.fixture(autouse=True)
def launch(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    driver.get("https://naveenautomationlabs.com/opencart/")
    driver.delete_all_cookies()
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
