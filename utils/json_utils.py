import base64
import json
import os


class JsonUtils:
    _current_dir = os.path.dirname(os.path.abspath(__file__))
    _file_path = os.path.join(_current_dir, '..', 'resources', 'apiData.json')

    @staticmethod
    def get_credentials() -> str:
        with open(JsonUtils._file_path) as f:
            test_data = json.load(f)
            client_id = test_data['client_id']
            client_secret = test_data['client_secret']
            client_credentials = f"{client_id}:{client_secret}"
        return base64.b64encode(client_credentials.encode()).decode()

