

class HotelModel:
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
