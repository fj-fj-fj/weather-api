from typing import Any

from requests import Session
from requests.models import Response

from settings import BaseConfiguration as config


class Client:

    def __init__(self) -> None:
        self._session: Session = Session()
        self._session.headers: dict = config.HEADERS
        self._service = {}

    @property
    def api_url(self) -> str:
        return ''.join(self._service.values())

    def run(self, city_name: str) -> dict[str, Any]:
        return self._call_current_weather_data_by_city_name(city_name).json()

    def _call_current_weather_data_by_city_name(
        self,
        city_name
    ) -> Response:
        return self._session.get(url=self.api_url.format(city_name))

    def __repr__(self):
        return (
            f'{type(self).__name__}'
            f'({self._session=!r} {self._session.headers=!r})'
        )
