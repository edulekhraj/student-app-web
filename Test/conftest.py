import os
import shutil
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from Utilities.utility import utility

# Function to clear the old Allure results
def clear_allure_results():
    allure_results_dir = "allure-results"  # Adjust the path if needed
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)  # Deletes the folder and its contents
    os.makedirs(allure_results_dir)  # Creates a fresh folder

# Run the clear function before pytest session starts
def pytest_sessionstart(session):
    clear_allure_results()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge", help="Type of browser. Default is chrome.")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(request, browser):
    global driver
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument('--disable-notifications')
        driver = webdriver.Edge(options=edge_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    url = utility.readConfig('Prod', 'url')
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
