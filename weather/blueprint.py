from flask import Blueprint


weather_api = Blueprint('weather_api', __name__)


@weather_api.route('/')
def index():
    return ''
