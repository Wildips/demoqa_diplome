import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv

from demoqa_diplome_tests.utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption("--browser-version", default=DEFAULT_BROWSER_VERSION)
    parser.addoption("--context", default="remote_selenoid")


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@allure.title("Настройка браузера для теста")
@pytest.fixture(scope="function", autouse=True)
def browser_session(request):
    browser_version = request.config.getoption("--browser-version")
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )

    context = request.config.getoption("--context")

    if context == "remote_selenoid":
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
        remote_browser_url = os.getenv("REMOTE_BROWSER_URL")

        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{remote_browser_url}/wd/hub",
            options=options,
        )

        browser.config.driver = driver

    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    if context == "remote_selenoid":
        attach.add_video(browser)

    browser.quit()
