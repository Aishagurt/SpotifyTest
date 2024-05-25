from browser.browser_name import BrowserName
from browser.local_browser_factory import LocalBaseBrowserFactory
from browser.py_quality_services import PyQualityServices
from core.configurations.interfaces.timeout_configuration_interface import ITimeoutConfiguration
from core.utilities.interfaces.action_repeater_interface import IActionRepeater
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver import Chrome, Firefox, Ie, Edge


class BrowserFactory(LocalBaseBrowserFactory):
    def __init__(self):
        super().__init__(PyQualityServices.browser_profile, PyQualityServices.localized_logger,
                         PyQualityServices.get(ITimeoutConfiguration), PyQualityServices.get(IActionRepeater))

    def get_driver(self) -> WebDriver:
        """Selecting the required driver (Firefox, Chrome and etc).
        :return: WebDriver.
        :rtype: WD.
        """
        browser_name = self._browser_profile.browser_name
        capabilities = self._browser_profile.get_driver_settings().get_capabilities()
        if browser_name == BrowserName.CHROME.value.lower():
            executable_path = ChromeDriverManager().install()
            service = ChromeService(executable_path)
            self.__driver = Chrome(service=service, options=capabilities)

        elif browser_name.lower() == BrowserName.FIREFOX.value.lower():
            executable_path = GeckoDriverManager().install()
            service = FirefoxService(executable_path=executable_path)
            self.__driver = Firefox(service=service, options=capabilities)

        elif browser_name.lower() == BrowserName.INTERNET_EXPLORER.value.lower():
            executable_path = IEDriverManager().install()
            service = IEService(executable_path=executable_path)
            self.__driver = Ie(service=service)

        elif browser_name.lower() == BrowserName.EDGE.value.lower():
            executable_path = EdgeChromiumDriverManager().install()
            service = EdgeService(executable_path=executable_path)
            self.__driver = Edge(service=service)

        return self.__driver
