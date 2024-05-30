import urllib.parse

from forms.base_form import BaseForm
from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices

class SearchForm(BaseForm):
    TRACK_NAME_LABEL_LOCATOR_FORMAT = "//*[contains(@href, '/track/') and .//*[contains(text(), '%s')]]"
    SEARCH_TRACKS_BUTTON_LOCATOR_FORMAT = "a[href='/search/%s/tracks']"
    _search_input = PyQualityServices.element_factory.get_text_box((By.CSS_SELECTOR, "form[role='search'] input"), "Search")


    def __init__(self):
        super().__init__((By.ID, "searchPage"), "Search")

    def get_song_text_by_name(self, search_text: str, song_name: str):
        self._search_input.type(search_text)
        self._search_input.submit()

        search_track_button = self._get_search_track_button(search_text)
        search_track_button.click()

        track_name_label = self._get_track_name_label(song_name)
        return track_name_label.text

    def _get_search_track_button(self, search_text: str):
        search_track_button_locator = (By.CSS_SELECTOR, self.SEARCH_TRACKS_BUTTON_LOCATOR_FORMAT % urllib.parse.quote(search_text))
        return self._element_factory.get_button(search_track_button_locator, "Search Track")

    def _get_track_name_label(self, song_name: str):
        track_name_label_locator = (By.XPATH, self.TRACK_NAME_LABEL_LOCATOR_FORMAT % song_name)
        return self._element_factory.get_label(track_name_label_locator, f"Track: {song_name}")