# test this json --> https://api.openweathermap.org/sample/weather_16.json.gz
import json
import sqlite3
from pathlib import Path

DB_NAME = 'test_sqlite.db'

ALL_CITIES_DATA = Path('../.story/weather_16.json')

filtered_service_data = {
    'id': 1,
    'url': 'https://api.openweathermap.org/',
}


class SQLiter:

    def __init__(self, db_name, file_path, services):
        # type: (object, str, Path, dict) -> None
        self.filtered_service_data = services
        self.file = file_path
        self.db = db_name
        self.cache = []

        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.connection.execute('pragma foreign_keys = 1')

    def run(self) -> object:
        self._create_tables()
        self._generate_data_to_dump_into_db()
        self._insert()
        return self

    def _create_tables(self) -> None:
        self.cursor.execute('drop table if exists weather')
        self.cursor.execute('drop table if exists service')
        self.cursor.execute('''
            create table if not exists service (
                id integer primary key autoincrement,
                name varchar(140))
            ''')
        self.cursor.execute('''
            create table if not exists weather (
                id integer primary key autoincrement,
                main varchar(140),
                description varchar(140),
                temperature float,
                pressure float,
                humidity float,
                temp_min float,
                temp_max float,
                wind_speed float,
                wind_deg float,
                clouds float,
                city_name varchar(140),
                country varchar(140),
                latitude float,
                longitude float,
                time varchar(20),
                service_id integer not null references service (id))
            ''')
        self.connection.commit()

    def _generate_data_to_dump_into_db(self) -> None:
        with open(self.file) as cities:
            self.filtered_weather_data = self._from_list_str_to_list_dict(
                cities.readlines())

            assert len(self.filtered_weather_data) == 209579
            assert self.filtered_weather_data[0]['id'] == 1
            assert self.filtered_weather_data[-1]['id'] == 209579

    def _insert(self) -> None:
        if self.filtered_service_data['url'] not in self.cache:
            self.cursor.execute(
                '''insert into service values (:id, :url)''',
                self.filtered_service_data)
        else:
            self.cache.append(self.filtered_service_data['url'])
        self.cursor.executemany(
            '''insert into weather values (
            :id, :main, :description, :temperature, :pressure,
            :humidity, :temp_min, :temp_max, :wind_speed,
            :wind_deg, :clouds, :city_name, :country, :latitude,
            :longitude, :time, :service_id)''',
            self.filtered_weather_data)
        self.connection.commit()

    def _from_list_str_to_list_dict(self, weather_data):
        # type: (list[str]) -> list[dict]
        return [{
            'id': index,
            'time': (j := json.loads(line))['time'],
            'main': (w := j['weather'][0])['main'],
            'temperature': (m := j['main'])['temp'],
            'city_name': (c := j['city'])['name'],
            'description': w['description'],
            'pressure': m['pressure'],
            'humidity': m['humidity'],
            'temp_min': m['temp_min'],
            'temp_max': m['temp_max'],
            'wind_speed': j['wind']['speed'],
            'wind_deg': j['wind']['deg'],
            'clouds': j['clouds']['all'],
            'country': c['country'],
            'latitude': c['coord']['lat'],
            'longitude': c['coord']['lon'],
            'service_id': 1,
        } for index, line in enumerate(weather_data, 1)]

    def display_count_all(self) -> None:
        self.cursor.execute('select count(*) from weather')
        cities = self.cursor.fetchall()
        self.cursor.execute('select * from service')
        services = self.cursor.fetchall()
        self.result_data_from_db = services, cities

        self._quit()
        print(self.result_data_from_db)

    def _quit(self) -> None:
        self.cursor.close()
        self.connection.close()


(db_worker := SQLiter(
    DB_NAME,
    ALL_CITIES_DATA,
    filtered_service_data
)).run().display_count_all()

assert db_worker.result_data_from_db[0][0][0] == 1
assert db_worker.result_data_from_db[1][0][0] == 209579

# >>> python3 test_sqlite.py
# ([(1, 'https://api.openweathermap.org/')], [(209579,)])
