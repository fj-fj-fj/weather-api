import gzip
from datetime import datetime
from typing import Any

from requests import Session
from requests.exceptions import SSLError
from requests.models import Response

from settings import APIConfiguration as config
from weather.database import db, recreate


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
            self._service._logger.exception(repr(e))
        except TypeError as e:
            self._service._logger.exception(repr(e))
        except SSLError as e:
            self._service._logger.exception(repr(e))
        self._parsed_data['Error'] = 'Something went wrong :('

    def __repr__(self):
        return (
            f'{type(self).__name__}'
            f'({self._session=!r} {self._session.headers=!r})')


class BulkDownloader:

    @property
    def remote_files_url(self) -> str:
        return ''.join(self._service_meta_bulk.values())

    def _download_full_data_file(self, *args, **kwargs) -> None:
        r = self._download_current_weather_data_by_all_cities()
        self._save_data_to_gz(r, *args, **kwargs)

    def _download_current_weather_data_by_all_cities(self) -> Response:
        return self._session.get(url=self.remote_files_url, stream=True)

    def _save_data_to_gz(self, r, *args, **kwargs) -> None:
        local_file = kwargs.get('local_file', 'weather_16.json.gz')
        with open(local_file, 'wb') as f:
            for chunk in r.raw.stream(1024, decode_content=False):
                if chunk:
                    f.write(chunk)

    def _save_data_to_db(self) -> None:
        # due to a circular import
        from weather.models import Service, Weather

        recreate(db)
        existing_service = Service.query.filter(
            Service.url == self.model.get('url')).first()
        if not existing_service:
            db.session.add(Service(**self.model))
            db.session.commit()
        # REFACTOR: ~ db.session.bulk_insert_mappings(Weather, mappings)
        for i, weather in enumerate((v for v in self._parsed_data.values())):
            db.session.add(Weather(**weather))
            if i and i % 1000 == 0:
                db.session.commit()
        db.session.commit()


class AllDataView(BulkDownloader):

    def show_all(self, *args, **kwargs) -> str:
        self.bulk = True

        if kwargs.get('fresh_data'):
            self._download_full_data_file(*args, **kwargs)

        self.bulk_downloads = self._read_data_from_gz(*args, **kwargs)
        self._try_to_parse_row_data()

        if kwargs.get('fresh_data') and self._parsed_data:
            self._save_data_to_db()

        return self._parsed_data

    def _read_data_from_gz(self, *args, **kwargs) -> str:
        local_file = kwargs.get('local_file', 'weather_16.json.gz')
        with gzip.open(local_file, 'rt') as f:
            return f.readlines()
