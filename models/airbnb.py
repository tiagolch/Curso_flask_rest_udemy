from sql_alchemy import db


class AirbnbModel(db.Model):
    __tablename__ = 'airbnb'

    airbnb_id = db.Column(db.String, primary_key=True)
    city = db.Column(db.String(100))
    state = db.Column(db.String(2))
    country = db.Column(db.String(100))
    price = db.Column(db.String(10))

    def __init__(self, airbnb_id, city, state, country, price):
        self.airbnb_id = airbnb_id
        self.city = city
        self.state = state
        self.country = country
        self.price = price

    def json(self):
        return {
            'airbnb_id': self.airbnb_id, 
            'city': self.city, 
            'state': self.state, 
            'country': self.country, 
            'price': self.price
        }

    @classmethod
    def find_airbnb(cls, airbnb_id):
        airbnb = cls.query.filter_by(airbnb_id=airbnb_id).first()
        if airbnb:
            return airbnb
        return None

    def save_airbnb(self):
        db.session.add(self)
        db.session.commit()

    def update_airbnb(self, city, state, country, price):
        self.city = city
        self.state = state
        self.country = country
        self.price = price

    def delete_airbnb(self):
        db.session.delete(self)
        db.session.commit()

