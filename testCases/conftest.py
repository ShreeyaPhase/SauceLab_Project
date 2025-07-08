import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        print("Lauching chrome")
        driver=webdriver.Chrome()
    elif browser=='firefox':
        print("Launching Firefox")
        driver=webdriver.Firefox()
    elif browser=='edge':
        print("Launching edge")
        driver=webdriver.Edge()
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()