import pytest
import requests

token=''

class TestYandexDisk:

    def setup_method(self):
        self.headers = {
            'Authorization': f'OAuth {token}'
        }


    @pytest.mark.parametrize(
        'param,value,status',
        (
            ['path', 'Image', 201],
            ['path', 'Image', 409],
        )
    )
    def test_folder(self, param, value, status):
        params = {param: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == status

