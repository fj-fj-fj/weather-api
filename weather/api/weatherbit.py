from logging import Logger

from settings import APIConfiguration as config
from weather.api.mixins import AllDataView, Client


class WeatherBit(Client, AllDataView):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._logger: Logger = Logger(__name__)
        self._service_meta: str = config.weatherbit_meta

    @property
    def url(self) -> str:
        return self._service_meta.get('url').removeprefix('https://api.')

    def _parse(self) -> None:
        data = self._weather_data['data'][0]

        self._parsed_data['city'] = data['city_name']
        self._parsed_data['time'] = data['ob_time']
        self._parsed_data['latitude'] = data['lat']
        self._parsed_data['longitude'] = data['lon']
        self._parsed_data['temperature'] = data['temp']

    # NOTE: bulk downloads implementation is missing due to
    # the lack of an example of the structure of  the downloaded file
