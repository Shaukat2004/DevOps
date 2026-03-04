import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser_name):

    if browser_name == "chrome":
        options = ChromeOptions()
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser_name == "edge":
        options = EdgeOptions()
        return webdriver.Edge(
            service=EdgeService("msedgedriver.exe"),
            options=options
        )

    else:
        raise Exception("Browser not supported")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run: chrome or edge"
    )

    