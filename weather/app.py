from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from settings.base import FlaskConfiguration
from weather.blueprint import weather_api
from weather.database import db

app = Flask(__name__)
app.config.from_object(FlaskConfiguration)
app.register_blueprint(weather_api, url_prefix='/api')

db.init_app(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
