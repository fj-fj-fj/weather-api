#!/bin/bash

FILE=.env

[ -e $FILE ] || (echo ".env file generating..." && touch .env)

echo setting FLASK_ENV, FLASK_APP, PROJECT_URL...
export FLASK_ENV=development
export FLASK_APP=main.py
export PROJECT_URL=http://127.0.0.1:5000

echo "# To use this file:" >> $FILE
echo "#     $ pip install python-dotenv" >> $FILE
echo "# Add this code to weather-api/settings/base.py:" >> $FILE
echo "#     from dotenv import load_dotenv" >> $FILE
echo "#     basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))" >> $FILE
echo "#     load_dotenv(os.path.join(basedir, '.env'))" >> $FILE
echo "#" >> $FILE
echo "# Remember never to commit secrets saved in .env files to Github." >> $FILE
echo "#" >> $FILE

echo FLASK_ENV=development >> $FILE
echo FLASK_APP=main.py >> $FILE
echo PROJECT_URL=http://127.0.0.1:5000 >> $FILE
echo OPENWEATHER_API_KEY=replace_the_values_with_your_values >> $FILE
echo WEATHERBIT_API_KEY=replace_the_values_with_your_values >> $FILE
