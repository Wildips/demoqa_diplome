import os
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv
from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"
DEMOQA_BASE_URL = "https://demoqa.com"

BROWSER_WIDTH = 1920
BROWSER_HEIGHT = 1080
BROWSER_TIMEOUT = 2.0


def pytest_addoption(parser):
    parser.addoption("--browser-version", default=DEFAULT_BROWSER_VERSION)
    parser.addoption("--context", default="remote_selenoid")


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@allure.title("Настройка браузера для теста")
@pytest.fixture(scope="function")
def browser_session(request):
    browser_version = request.config.getoption("--browser-version")
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )

    context = request.config.getoption("--context")

    if context == "remote_selenoid":
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")

        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options,
        )

        browser.config.driver = driver

    browser.config.base_url = DEMOQA_BASE_URL
    browser.config.timeout = BROWSER_TIMEOUT
    browser.config.window_width = BROWSER_WIDTH
    browser.config.window_height = BROWSER_HEIGHT

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
