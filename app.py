from flask import Flask

from weather.blueprint import weather_api


app = Flask(__name__)

app.register_blueprint(weather_api, url_prefix='/api')
