from flask_restful import Resource, reqparse
from models.hotel import HotelModel


hoteis = [
    {'hotel_id': 'Alpha', 'nome': 'Alpha Hotel', 'endereco': 'Rua Alpha, 100'},
    {'hotel_id': 'Bravo', 'nome': 'Bravo Hotel', 'endereco': 'Rua Bravo, 200'},
    {'hotel_id': 'Charlie', 'nome': 'Charlie Hotel', 'endereco': 'Rua Charlie, 300'},
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome')
    parser.add_argument('endereco')


    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None


    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'erro': 'hotel_id nao encontrado'}, 404
        
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel id {hotel_id} already exists.'}, 400

        data = Hotel.parser.parse_args()
        hotel = HotelModel(hotel_id, **data) 
        hotel.save_hotel()
        return hotel.json(), 201


    def put(self, hotel_id):
        data = Hotel.parser.parse_args()

        object_hotel = HotelModel(hotel_id, **data)     
        new_hotel = object_hotel.json()

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hoteis.append(new_hotel)
        return new_hotel, 201
        

    def delete(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hoteis.remove(hotel)
            return {'hoteis': hoteis}, 200
        return {'erro': f'hotel_id {hotel_id} nao encontrado'}, 404

