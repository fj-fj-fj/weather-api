# test this json --> https://api.openweathermap.org/sample/weather_16.json.gz
import json
from pathlib import Path

from weather.app import db
from weather.models import Service, Weather


def format_data(file: Path) -> list[str]:
    with open(file) as all:
        filtered_weather_data = from_list_str_to_list_dict(
            all.readlines())

        assert len(filtered_weather_data) == 209579
    return filtered_weather_data


def from_list_str_to_list_dict(weather_data):
    # type: (list[str]) -> list[dict]
    return [{
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
    } for line in weather_data]


db.drop_all()
db.create_all()

db.session.add(Service(url='https://api.openweathermap.org/'))
db.session.commit()
print('Service count:', Service.query.count())

db.session.bulk_insert_mappings(
    Weather,
    format_data(Path('../.story/weather_16.json')))
db.session.commit()
print('Weather count:', Weather.query.count())

assert Service.query.count() == 1
assert Weather.query.count() == 209579
