
import pytest
from pageObjects.home_form import HomeForm
from pageObjects.search_form import SearchForm
from conftest import browser
from resources.constants.ui_constants import UrlConstant
from resources.constants.common_constants import SingerName, Song


class TestSongAvailability:
    home_form: HomeForm = HomeForm()
    search_form: SearchForm = SearchForm()

    @pytest.mark.parametrize("singer_name, song_name",
                             [
                                 pytest.param(SingerName.DRAKE.value, Song.ONE_DANCE.value),
                                 pytest.param(SingerName.THE_BEATLES.value, Song.HERE_COMES_THE_SUN.value)
                             ])
    def test_check_song(self, browser, singer_name, song_name):
        browser.go_to(url=UrlConstant.SPOTIFY_HOME_PAGE)

        assert self.home_form.is_displayed()

        self.home_form.go_to_search_page()

        assert self.search_form.is_displayed()

        song_text = self.search_form.get_song_text_by_name(search_text=singer_name, song_name=song_name)

        assert song_text.lower() == song_name.lower(), f"Wrong name for the song {song_name}"
