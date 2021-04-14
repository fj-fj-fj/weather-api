from weather.app import db, ma


class Service(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    weather = db.relationship(
        'Weather',
        backref=db.backref('service', passive_deletes=True))

    def __repr__(self):
        return f'{type(self).__name__}({self.id!r}, {self.url!r})'


class Weather(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey(
        'service.id', ondelete='cascade'))

    city_name = db.Column(db.String(80), index=True)
    country = db.Column(db.String(5))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    main = db.Column(db.String(20), index=True)
    description = db.Column(db.String(40))
    clouds = db.Column(db.Float)
    temperature = db.Column(db.Float, index=True)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    pressure = db.Column(db.Float)
    humidity = db.Column(db.Float)
    wind_speed = db.Column(db.Float)
    wind_deg = db.Column(db.Float)
    time = db.Column(db.String(30), index=True)

    def __repr__(self):
        return (f'{type(self).__name__}({self.city_name!r}, '
                f'{self.temperature!r}, {self.description!r})')


class ServiceSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Service
        sqla_session = db.session


class WheatherSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Weather
        include_fk = True
        sqla_session = db.session
