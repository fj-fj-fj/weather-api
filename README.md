# Weather API

[![Flask](https://img.shields.io/badge/-flask-red?style=flat&logo=flask)](https://palletsprojects.com/p/flask/)
[![CI](https://github.com/fj-fj-fj/weather-api/actions/workflows/ci.yml/badge.svg)](https://github.com/fj-fj-fj/weather-api/actions/workflows/ci.yml)


## Introduction
The app gets and stores a list of values provided by [OpenWeather](https://openweathermap.org/) [Weatherbit.io](https://www.weatherbit.io/) and provides a `route` for the frontend for a GET-request. Route contains the list of stored values _(city, time, latitude, longitude, temperature and the site from which the information was originally obtained)_

## Instalation
```bash
git clone https://github.com/fj-fj-fj/weather-api.git
cd weather-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export FLASK_DEBUG=True
export FLASK_ENV=development
export FLASK_APP=main.py
export OPENWEATHER_API_KEY=your_openwheather_api_key
export WEATHERBIT_API_KEY=your_weatherbit_api_key

flask run
```
Enter [`http://127.0.0.1:5000/api`](http://127.0.0.1:5000/api)

#
The default name of the city is Moscow. Change it here: /weather/api/blueprint/index.city_name
