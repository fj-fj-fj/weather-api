from flask import Blueprint, jsonify
from flask.wrappers import Response

from weather.api import openweater_service, weatherbit_service


weather_api = Blueprint('weather_api', __name__)


@weather_api.route('/')
def index() -> Response:
    city_name = 'London'
    return jsonify({
        'openweather.com': openweater_service.run(city_name),
        'weatherbit.io': weatherbit_service.run(city_name),
    })
