from datetime import datetime, timedelta
from typing import Any

from requests import Session
from requests.exceptions import SSLError
from requests.models import Response

from settings import BaseConfiguration as config


class Client:

    def __init__(self, service, *args, **kwargs) -> None:
        self._session: Session = Session()
        self._session.headers: dict = config.HEADERS
        self._service: object = service
        self._service_meta = {}
        self._weather_data = {}
        self._parsed_data = {}

    @staticmethod
    def form_time(timestamp: str) -> datetime:
        return datetime.fromtimestamp(timestamp)

    @property
    def api_url(self) -> str:
        return ''.join(self._service_meta.values())

    def run(self, city_name: str) -> dict[str, Any]:
        self._parse_weather_data(city_name)
        return self._parsed_data

    def _parse_weather_data(self, city_name: str) -> None:
        self._set_weather_data(city_name)
        self._try_to_parse_row_data()

    def _set_weather_data(self, city_name: str) -> None:
        self._weather_data = self._call_current_weather_data_by_city_name(
            city_name
        ).json()

    def _call_current_weather_data_by_city_name(
        self,
        city_name: str
    ) -> Response:
        return self._session.get(url=self.api_url.format(city_name))

    def _try_to_parse_row_data(self) -> None:
        try:
            return self._service._parse()
        except KeyError as e:
            self._service._logger.fatal(e)
        except TypeError as e:
            self._service._logger.fatal(e)
        except SSLError as e:
            self._service._logger.fatal(e)
        self._parsed_data['Error'] = 'Something went wrong :('

    def __repr__(self):
        return (
            f'{type(self).__name__}'
            f'({self._session=!r} {self._session.headers=!r})'
        )
