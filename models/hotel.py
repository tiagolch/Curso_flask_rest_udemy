from sql_alchemy import db

class HotelModel(db.Model):
    __tablename__ = 'hoteis'
    
    hotel_id = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(100))


    def __init__(self, hotel_id, nome, endereco):
        self.hotel_id = hotel_id
        self.nome = nome
        self.endereco = endereco

    def json(self):
        return {
            'hotel_id': self.hotel_id, 
            'nome': self.nome, 
            'endereco': self.endereco
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None
        
    def save_hotel(self):
        db.session.add(self)
        db.session.commit()

    def update_hotel(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def delete_hotel(self):
        db.session.delete(self)
        db.session.commit()
