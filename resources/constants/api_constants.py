class EndPointConstant:
    BASE_API_ENDPOINT: str = "https://api.spotify.com/v1"
    BASE_TOKEN_ENDPOINT: str = "https://accounts.spotify.com/api/token"
    AVAILABLE_MARKETS_ENDPOINT: str = f"{BASE_API_ENDPOINT}/markets"
    SEARCH_ENDPOINT: str = f"{BASE_API_ENDPOINT}/search?"


class HttpStatusCodeConstant:
    OK: int = 200


class ParameterConstant:
    GRANT_TYPE = "grant_type"
    QUERY = "q"
    SEARCH_TYPE = "type"
    AUTHORIZATION = "Authorization"


class ParameterValueConstant:
    TOKEN_TYPE = "token_type"
    ACCESS_TOKEN = "access_token"
    ARTIST_PARAMETER_VALUE = "artist"
    CLIENT_CREDENTIALS = "client_credentials"
    AUTHORIZATION_VALUE = f"Basic %s"
    SEARCH_TYPE_VALUE = "artist"
