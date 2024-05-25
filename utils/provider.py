import random
from typing import List
from urllib.parse import urlencode

from requests import Session

from models.artist import Artist
from models.track import Track
from resources.constants.api_constants import EndPointConstant, HttpStatusCodeConstant, ParameterConstant, \
    ParameterValueConstant
from utils.json_utils import JsonUtils


class SpotifyProvider:
    __session: Session

    @property
    def session(self) -> Session:
        if not hasattr(self, "__session"):
            self.__session = Session()
            response = self.__session.post(
                EndPointConstant.BASE_TOKEN_ENDPOINT,
                data={ParameterConstant.GRANT_TYPE: ParameterValueConstant.CLIENT_CREDENTIALS},
                headers={ParameterConstant.AUTHORIZATION: ParameterValueConstant.AUTHORIZATION_VALUE
                                                          % JsonUtils.get_credentials()}
            )
            assert response.status_code == HttpStatusCodeConstant.OK, "Failed to login"
            auth_data = response.json()
            self.__session.headers.update(
                {ParameterConstant.AUTHORIZATION: f"{auth_data[ParameterValueConstant.TOKEN_TYPE]} "
                                                  f"{auth_data[ParameterValueConstant.ACCESS_TOKEN]}"})
        return self.__session

    def find_available_markets(self) -> List[str]:
        response = self.session.get(EndPointConstant.AVAILABLE_MARKETS_ENDPOINT)
        return response.json()["markets"]

    def get_artist_by_name(self, artist_name: str) -> List[Artist]:
        query_data = urlencode({ParameterConstant.QUERY: artist_name,
                                ParameterConstant.SEARCH_TYPE: ParameterValueConstant.SEARCH_TYPE_VALUE})
        response = self.session.get(f"{EndPointConstant.SEARCH_ENDPOINT}{query_data}")
        assert response.status_code == HttpStatusCodeConstant.OK, "Failed to get artist data"
        artist_list = response.json()["artists"]["items"]
        return [Artist.create_model(artist_data) for artist_data in artist_list]

    def get_top_tracks_by_artist(self, artist: Artist) -> List[Track]:
        query_data = urlencode({"market": random.choice(self.find_available_markets())})
        response = self.session.get(f"{EndPointConstant.BASE_API_ENDPOINT}/artists/{artist.id}/top-tracks?{query_data}")
        top_tracks = response.json()["tracks"]
        return [Track.create_model(track_data) for track_data in top_tracks]
