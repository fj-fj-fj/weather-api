from logging import Logger

from settings import BaseConfiguration as base
from weather.api.mixins import Client


class WeatherBit(Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger: Logger = Logger(__name__)
        self._service: str = base.weatherbit_meta
