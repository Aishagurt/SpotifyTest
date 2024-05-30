import pytest

from resources.constants.common_constants import SingerName, Genre, Song
from utils.provider import SpotifyProvider


class TestArtistsApi:
    provider: SpotifyProvider = SpotifyProvider()

    @pytest.mark.parametrize("artist_name, artist_genre",
                             [
                                 pytest.param(SingerName.DRAKE.value, Genre.RAP.value),
                                 pytest.param(SingerName.THE_BEATLES.value, Genre.BRITISH_INVASION.value)
                             ])
    def test_check_artists_genre(self, artist_name: str, artist_genre: str):
        artists = self.provider.get_artist_by_name(artist_name=artist_name)

        certain_artist = None
        for artist in artists:
            if artist.name.lower() == artist_name.lower():
                certain_artist = artist
                break

        assert certain_artist is not None, f"No artist found with the name '{artist_name}'"
        assert artist_genre in certain_artist.genres, f"The artist '{artist_name}' does not have the genre '{artist_genre}'"

    @pytest.mark.parametrize("artist_name, expected_song",
                             [
                                 pytest.param(SingerName.DRAKE.value, Song.ONE_DANCE.value),
                                 pytest.param(SingerName.THE_BEATLES.value, Song.HERE_COMES_THE_SUN.value)
                             ])
    def test_check_artists_the_most_popular_song(self, artist_name: str, expected_song: str):
        artists = self.provider.get_artist_by_name(artist_name=artist_name)

        certain_artist = None
        for artist in artists:
            if artist.name.lower() == artist_name.lower():
                certain_artist = artist
                break

        assert certain_artist is not None, f"No artist found with the name '{artist_name}'"

        top_tracks = self.provider.get_top_tracks_by_artist(artist=certain_artist)

        certain_song = None
        for track in top_tracks:
            if track.name.lower() == expected_song.lower():
                certain_song = track
                break

        assert certain_song is not None, f"Track {expected_song} is not in top tracks of {artist_name}"
