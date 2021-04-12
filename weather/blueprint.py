from flask import Blueprint
from flask.wrappers import Response

from weather.api import openweater_service, weatherbit_service


weather_api = Blueprint('weather_api', __name__)


@weather_api.route('/')
def fetch_current_weater_by_city_name() -> Response:
    city_name = 'Moscow'
    return {
        'openweather.com': openweater_service.run(city_name),
        'weatherbit.io': weatherbit_service.run(city_name),
    }


@weather_api.route('/all-data/')
def show_weather_data_of_all_cities() -> Response:
    return dict({
        'openweather.com': openweater_service.show_all(fresh_data=True),
        # ACSSES IS DENIED
        # 'weatherbit.io': weatherbit_service.show_all(fresh_data=None),
    })
