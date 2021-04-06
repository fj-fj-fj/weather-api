from datetime import datetime
from logging import Logger

from settings import BaseConfiguration as config
from weather.api.mixins import Client


class OpenWeather(Client):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self._logger: Logger = Logger(__name__)
        self._service_meta: dict = config.openweather_meta

    def _parse(self) -> None:
        data: dict = self._weather_data
        time: datetime = self.form_time(data['timezone'])

        self._parsed_data['city'] = data['name']
        self._parsed_data['time'] = str(time)
        self._parsed_data['latitude'] = data['coord']['lat']
        self._parsed_data['longitude'] = data['coord']['lon']
