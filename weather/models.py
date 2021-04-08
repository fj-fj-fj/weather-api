import re
from datetime import datetime

from weather.app import db


class Weather(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    temp = db.Column(db.Float)
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.slug = self.generate_slug()

    def generate_slug(self) -> str:
        if self.city:
            pattern = r'[^\w+]'
            return re.sub(pattern, '-', self.city)

    def __repr__(self):
        return f'{type(self).__name__} (id: {self.id!r}, city: {self.city!r})'
