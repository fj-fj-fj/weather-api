import pytest
import requests
from os import getenv
from unittest import skipIf
from unittest.mock import Mock, patch

from weather.api.openweather import _cut_substring_after_pattern

REAL_SERVER = getenv('SKIP_REAL', False)
OPENWEATHER_API_KEY = getenv('OPENWEATHER_API_KEY')
API_URL_WITH_MOSCOW_CITY = f'https://api.openweathermap.org/data/2.5/weather?q=moscow&units=metric&appid={OPENWEATHER_API_KEY}'

bulk_data_item = '{"city":{"id":14256,"name":"Azadshahr","findname":"AZADSHAHR","country":"IR","coord":{"lon":48.570728,"lat":34.790878},"zoom":10},"time":1554462304,"main":{"temp":287.07,"pressure":1022,"humidity":71,"temp_min":284.15,"temp_max":289.15},"wind":{"speed":4.1,"deg":340},"clouds":{"all":90},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}]}'
moscow_weather = {"coord":{"lon":37.6156,"lat":55.7522},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":5.08,"feels_like":-0.8,"temp_min":4,"temp_max":6.11,"pressure":1004,"humidity":65},"visibility":10000,"wind":{"speed":12,"deg":250},"clouds":{"all":75},"dt":1619343150,"sys":{"type":1,"id":9027,"country":"RU","sunrise":1619316005,"sunset":1619369676},"timezone":10800,"id":524901,"name":"Moscow","cod":200}


@pytest.mark.parametrize(
    'key, bulk_data_item, expected',
    [
        ('name', bulk_data_item, 'Azadshahr'),
        ('description', bulk_data_item, 'overcast clouds'),
        ('temp', bulk_data_item, '287.07'),
        ('temp_min', bulk_data_item, '284.15'),
        ('temp_max', bulk_data_item, '289.15'),
        ('pressure', bulk_data_item, '1022'),
        ('humidity', bulk_data_item, '71'),
        ('speed', bulk_data_item, '4.1'),
        ('deg', bulk_data_item, '340'),
        ('all', bulk_data_item, '90'),
        ('country', bulk_data_item, 'IR'),
        ('lon', bulk_data_item, '48.570728'),
        ('lat', bulk_data_item, '34.790878'),
        ('time', bulk_data_item, '1554462304'),
    ]
)
def test_cut_substring_after_pattern(key, bulk_data_item, expected):
    return _cut_substring_after_pattern(key, bulk_data_item) == expected


class TestOpenWeatherAPI(object):

    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_request_response(self):
        self.mock_get.return_value.ok = True
        response = requests.get('https://api.openweathermap.org/')
        assert response.ok

    def test_getting_weather_by_city_when_response_is_ok(self):
        self.mock_get.return_value = Mock(ok=True)
        self.mock_get.return_value.json.return_value = moscow_weather
        response = requests.get(API_URL_WITH_MOSCOW_CITY)
        assert response.json() == moscow_weather

    def test_getting_weather_by_city_when_response_is_not_ok(self):
        self.mock_get.return_value.ok = False
        response = requests.get(API_URL_WITH_MOSCOW_CITY)
        assert not response.ok


@skipIf(REAL_SERVER, 'Skipping tests that hit the real API server.')
def test_actual_and_mocked_api_have_some_data_srtucture():
    actual = requests.get(API_URL_WITH_MOSCOW_CITY)
    actual_keys = actual.json().keys()

    with patch('requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = moscow_weather

        mocked = requests.get(API_URL_WITH_MOSCOW_CITY)
        mocked_keys = mocked.json().keys()

    assert actual_keys == mocked_keys


# REFACTOR: replace patch 'requests.get' to 'OpenWeather._call_current_weather_data_by_city_name'
