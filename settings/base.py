import logging
import os

logging.basicConfig(level=logging.DEBUG)
for logger in ('urllib3', 'werkzeug'):
    logging.getLogger(logger).setLevel(logging.WARNING)


class BaseConfiguration:

    API_KEYS = {
        'OPENWEATHER_API_KEY': os.getenv('OPENWEATHER_API_KEY'),
        'WEATHERBIT_API_KEY': os.getenv('WEATHERBIT_API_KEY'),
    }

    HEADERS = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            'AppleWebKit/537.36 (KHTML, like Gecko)'
            'Chrome/88.0.4324.182 Safari/537.36'
        ),
        'accept': '*/*',
    }

    # 'https://openweathermap.org/current#current_JSON'
    # 'https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/Current32Weather32Data/get_current_city_id_city_id'

    BASE_URLS = {
        'OPENWEATHER': 'https://api.openweathermap.org/',
        'WEATHERBIT': 'https://api.weatherbit.io/',
    }

    openweather_meta = {
        'url': BASE_URLS['OPENWEATHER'],
        'parameters': 'data/2.5/weather?q={}&appid=',
        'key': API_KEYS['OPENWEATHER_API_KEY'],
    }

    weatherbit_meta = {
        'url': BASE_URLS['WEATHERBIT'],
        'parameters': 'v2.0/current?city={}&key=',
        'key': API_KEYS['WEATHERBIT_API_KEY'],
    }
    # NOTE:(Advanceed/Enterprise plans only) Examples of bulk files
    openweather_meta_bulk = {
        'url': BASE_URLS['OPENWEATHER'].replace('api', 'bulk'),
        'parameters': 'sample/weather_16.json.gz',
        # 'key': API_KEYS['OPENWEATHER_API_KEY'],
    }

    # NOTE:(Advanceed/Enterprise plans only) THIS HAS NO EXAMPLE!
    weatherbit_meta_bulk = {
        'url': BASE_URLS['WEATHERBIT'],
        'parameters': 'v2.0/bulk/files/current.json.gz?key=',
        # 'key': API_KEYS['WEATHERBIT_API_KEY'],
    }
