

class AirbnbModel:
    def __init__(self, airbnb_id, city, state, country, price,):
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
        

