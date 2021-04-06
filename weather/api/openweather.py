from logging import Logger

from settings import BaseConfiguration as config
from weather.api.mixins import Client


class OpenWeather(Client):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._logger: Logger = Logger(__name__)
        self._service: dict = config.openweather_meta
