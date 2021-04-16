# Weather API

[![Python](https://img.shields.io/static/v1?label=Python&style=plastic&logofor-the-badge&message=v^3.9&color=3776AB&logo=PYTHON)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-flask-red?style=flat&logo=flask)](https://palletsprojects.com/p/flask/)
[![CI](https://github.com/fj-fj-fj/weather-api/actions/workflows/ci.yml/badge.svg)](https://github.com/fj-fj-fj/weather-api/actions/workflows/ci.yml)


## Introduction
The app gets and stores a list of values provided by [OpenWeather](https://openweathermap.org/) [Weatherbit.io](https://www.weatherbit.io/) and provides a `route` for the frontend for a GET-request. Route contains the list of stored values _(city, time, latitude, longitude, temperature and the site from which the information was originally obtained)_

## Instalation
```bash
# Before start export this variables when on test or production according to your environment
$ export OPENWEATHER_API_KEY=your_openwheather_api_key
$ export WEATHERBIT_API_KEY=your_weatherbit_api_key

$ git clone https://github.com/fj-fj-fj/weather-api.git
$ cd weather-api
$ make
```
Enter [`http://127.0.0.1:5000/api`](http://127.0.0.1:5000/api)


The default name of the city is Moscow. Change it here: /weather/api/blueprint/index

#
Add city name e.g., [`http://127.0.0.1:5000/api/london`](http://127.0.0.1:5000/api/london)

```json
{
  "openweathermap.org/": {
    "city": "London",
    "latitude": 51.5085,
    "longitude": -0.1257,
    "temperature": 3.78,
    "time": "2021-04-16 02:04"
  },
  "weatherbit.io/": {
    "city": "London",
    "latitude": 35.32897,
    "longitude": -93.25296,
    "temperature": 18.9,
    "time": "2021-04-15 22:27"
  }
}
```
## Database
Saving to a database with more complete information has also been implemented.

```bash
# I used MySQL and mysql-connector-python and here are my steps
$ mysql --user=user_name --password=your_password

mysql> create database weather_api character set utf8 collate utf8_unicode_ci;
mysql> exit;

$ export SQLALCHEMY_TRACK_MODIFICATIONS=False
$ export SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://user_name:your_password@localhost/weather_api
$ echo SQLALCHEMY_TRACK_MODIFICATIONS=False >> .env
$ echo SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://my_name:my_password@localhost/weather_api >> .env
$ source .venv/bin/activate  # if not activated yet
$ flask shell
```
```python-repl
>>> from weather.app import db
>>> db.create_all()
>>> exit()
```
```bash
$ flask run
```
