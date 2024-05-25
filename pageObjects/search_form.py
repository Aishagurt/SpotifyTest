import urllib.parse
from forms.base_form import BaseForm
from selenium.webdriver.common.by import By


class SearchForm(BaseForm):
    SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, "form[role='search'] input")
    TRACK_NAME_LABEL_LOCATOR_FORMAT = "//*[contains(@href, '/track/') and .//*[contains(text(), '%s')]]"
    SEARCH_TRACKS_BUTTON_LOCATOR_FORMAT = "a[href='/search/%s/tracks']"

    def __init__(self):
        super().__init__((By.ID, "searchPage"), "Search")

    def get_song_by_name(self, search_text: str, song_name: str):
        search_input = self._element_factory.get_text_box(self.SEARCH_INPUT_LOCATOR, "Search")

        search_input.type(search_text)
        search_input.submit()

        search_track_link_locator = (By.CSS_SELECTOR, self.SEARCH_TRACKS_BUTTON_LOCATOR_FORMAT % urllib.parse.quote(search_text))
        search_track_link = self._element_factory.get_button(search_track_link_locator, "Search Track")
        search_track_link.click()

        track_name_label_locator = (By.XPATH, self.TRACK_NAME_LABEL_LOCATOR_FORMAT % song_name)
        track_name_label = self._element_factory.get_label(track_name_label_locator, "Track")

        return track_name_label
