
import pytest
from pageObjects.home_form import HomeForm
from pageObjects.search_form import SearchForm
from conftest import browser
from resources.constants.ui_constants import UrlConstant
from resources.constants.common_constants import SingerNameConstant, SongConstant


class TestSongAvailability:
    home_form: HomeForm = HomeForm()
    search_form: SearchForm = SearchForm()

    @pytest.mark.parametrize("singer_name, song_name",
                             [
                                 pytest.param(SingerNameConstant.DRAKE, SongConstant.ONE_DANCE),
                                 pytest.param(SingerNameConstant.THE_BEATLES, SongConstant.HERE_COMES_THE_SUN)
                             ])
    def test_check_song(self, browser, singer_name: str, song_name: str):
        browser.go_to(url=UrlConstant.SPOTIFY_HOME_PAGE)

        assert self.home_form.is_displayed()

        self.home_form.go_to_search_page()

        assert self.search_form.is_displayed()

        song_text_box = self.search_form.get_song_by_name(search_text=singer_name, song_name=song_name)

        assert song_text_box.text.lower() == song_name.lower(), f"Wrong name for the song {song_name}"
