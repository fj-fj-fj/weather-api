from datetime import datetime
from logging import Logger

import pytemperature

from settings import APIConfiguration as config
from weather.api.mixins import Client, AllDataView


class OpenWeather(Client, AllDataView):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self._logger: Logger = Logger(__name__)
        self._service_meta: dict = config.openweather_meta
        self._service_meta_bulk: dict = config.openweather_meta_bulk

    def _parse(self) -> None:
        data: dict = self._weather_data
        time: datetime = self.form_time(data['dt'])
        temperature = pytemperature.k2c(data['main']['temp'])

        self._parsed_data['city'] = data['name']
        self._parsed_data['time'] = f'{time:%Y-%m-%d %H:%M}'
        self._parsed_data['latitude'] = data['coord']['lat']
        self._parsed_data['longitude'] = data['coord']['lon']
        self._parsed_data['temperature'] = round(temperature)
