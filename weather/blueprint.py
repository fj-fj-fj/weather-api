from flask import Blueprint, jsonify, make_response
from flask.wrappers import Response

from weather.api import openweater_service as openweather
from weather.api import weatherbit_service as weatherbit

weather_api = Blueprint('weather_api', __name__)


@weather_api.route('/', defaults={'city_name': 'Moscow'})
@weather_api.route('/<string:city_name>')
def fetch_current_weater_by_city_name(city_name: str) -> Response:
    response = {
        openweather.url: openweather.run(city_name),
        weatherbit.url: weatherbit.run(city_name),
    }
    headers = {'Content-Type': 'application/json'}
    return make_response(jsonify(response), 200, headers)


@weather_api.route('/all-data/')
def show_weather_data_of_all_cities() -> Response:
    response = {
        # bulk downloading and saving if fresh_data=True
        # else read old data from file or select * from db
        openweather.url: openweather.show_all(fresh_data=True),
        # ACSSES IS DENIED
        # weatherbit.url: weatherbit.show_all(fresh_data=None),
    }
    headers = {'Content-Type': 'application/json'}
    return make_response(jsonify(response), 200, headers)
