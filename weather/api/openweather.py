import re
from datetime import datetime
from logging import Logger

from settings import APIConfiguration as config
from weather.api.mixins import Client, AllDataView


def _cut_substring_after_pattern(key: str, string: str) -> str:
    # search and return substring or float or int after key
    result = re.search(
        fr'(?<=\"{key}\":)("([^\"]*)"+|[-+]?([0-9]*[.,]?[0-9]+|[0-9]+))',
        string)
    try:
        return result.group()
    except AttributeError:
        raise AttributeError(
            f"'NoneType' object has no attribute 'group', {key=}, {string=}")


class OpenWeather(Client, AllDataView):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self._logger: Logger = Logger(__name__)
        self._service_meta: dict = config.openweather_meta
        self._service_meta_bulk: dict = config.openweather_meta_bulk
        self.model = self._generate_fields()
        self.bulk_downloads = ''
        self.bulk = False

    def _parse(self) -> None:
        if not self.bulk:
            data: dict = self._weather_data
            time: datetime = self.form_time(data['dt'])

            self._parsed_data['city'] = data['name']
            self._parsed_data['time'] = f'{time:%Y-%m-%d %H:%M}'
            self._parsed_data['latitude'] = data['coord']['lat']
            self._parsed_data['longitude'] = data['coord']['lon']
            self._parsed_data['temperature'] = data['main']['temp']

            return

        for line in self.bulk_downloads:
            city = self._set_value('name', line)

            self._parsed_data |= {city: {
                'city_name': city,
                'main': self._set_value('main', line),
                'description': self._set_value('description', line),
                'temperature': self._set_value('temp', line),
                'temp_min': self._set_value('temp_min', line),
                'temp_max': self._set_value('temp_max', line),
                'pressure': self._set_value('pressure', line),
                'humidity': self._set_value('humidity', line),
                'wind_speed': self._set_value('speed', line),
                'wind_deg': self._set_value('deg', line),
                'clouds': self._set_value('all', line),
                'country': self._set_value('country', line),
                'longitude': self._set_value('lon', line),
                'latitude': self._set_value('lat', line),
                'time': self._set_value('time', line),
                'service_id': self.model.get('id')}}

    def _set_value(self, *args, **kwargs) -> str:
        return _cut_substring_after_pattern(*args, **kwargs)

    def _generate_fields(self) -> dict:
        return {'id': 1, 'url': self._service_meta.get('url')}
