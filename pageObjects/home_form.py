from forms.base_form import BaseForm
from selenium.webdriver.common.by import By


class HomeForm(BaseForm):
    __SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "a[aria-label='Search']")

    def __init__(self):
        super(HomeForm, self).__init__((By.CSS_SELECTOR, "section[data-testid='home-page']"), "Home")

    def go_to_search_page(self):
        self._element_factory.get_button(self.__SEARCH_BUTTON_LOCATOR, "Search").click()
