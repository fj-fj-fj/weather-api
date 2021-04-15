# Weather API

[![Flask](https://img.shields.io/badge/-flask-red?style=flat&logo=flask)](https://palletsprojects.com/p/flask/)
[![CI](https://github.com/fj-fj-fj/weather-api/actions/workflows/ci.yml/badge.svg)](https://github.com/fj-fj-fj/weather-api/actions/workflows/ci.yml)


## Introduction
The app gets and stores a list of values provided by [OpenWeather](https://openweathermap.org/) [Weatherbit.io](https://www.weatherbit.io/) and provides a `route` for the frontend for a GET-request. Route contains the list of stored values _(city, time, latitude, longitude, temperature and the site from which the information was originally obtained)_

## Instalation
```bash
$ git clone https://github.com/fj-fj-fj/weather-api.git
$ cd weather-api
$ ./install.sh
$ python3  # or python

$ export FLASK_ENV=development
$ export FLASK_APP=main.py
$ export PROJECT_URL=http://127.0.0.1:5000
$ export OPENWEATHER_API_KEY=your_openwheather_api_key
$ export WEATHERBIT_API_KEY=your_weatherbit_api_key

$ flask run
```
Enter [`http://127.0.0.1:5000/api`](http://127.0.0.1:5000/api)


The default name of the city is Moscow. Change it here: /weather/api/blueprint/index

#
Add city name e.g., [`http://127.0.0.1:5000/api/london`](http://127.0.0.1:5000/api/london)

```
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
Saving to a database with more complete information has also been implemented.
