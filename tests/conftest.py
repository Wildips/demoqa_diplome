import os
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selene.support.shared import browser

from selene import Browser, Config
from selene import Config, browser

from dotenv import load_dotenv

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption("--browser-version", default=DEFAULT_BROWSER_VERSION)


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@allure.title("Настройка браузера")
# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture(scope="function")
def browser_session(request):
    browser_version = request.config.getoption("--browser-version")
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        # command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    # !!!!
    browser.config.driver = driver

    # browser = Browser(Config(driver))

    # browser.driver.base_url = "https://demoqa.com"
    # browser.driver.timeouts = 2.0
    # browser.driver.window_width = 1920
    # browser.driver.window_height = 1080

    # selenoid
    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
