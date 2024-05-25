import pytest
from browser.browser import Browser
from browser.py_quality_services import PyQualityServices
from utils.browser_factory import BrowserFactory


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()

@pytest.fixture(scope="session")
def browser() -> Browser:
    browser = PyQualityServices.get_browser()
    browser.maximize()
    yield browser
    browser.quit()