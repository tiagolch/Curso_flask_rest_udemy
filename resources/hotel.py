from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True, help='Nome do hotel')
    parser.add_argument('endereco', type=str, required=True, help='Endereco do hotel')



    def get(self, hotel_id):
        hotel_located = HotelModel.find_hotel(hotel_id)
        if hotel_located:
            return hotel_located.json(), 200
        return {'erro': 'hotel_id nao encontrado'}, 404
        
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel id {hotel_id} already exists.'}, 400

        data = Hotel.parser.parse_args()
        hotel = HotelModel(hotel_id, **data) 
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An error occurred inserting the hotel.'}, 500
        return hotel.json(), 201


    def put(self, hotel_id):

        data = Hotel.parser.parse_args()

        hotel_located = HotelModel.find_hotel(hotel_id)
        if hotel_located:
            hotel_located.update_hotel(**data)
            hotel_located.save_hotel()
            return hotel_located.json(), 200
        hotel = HotelModel(hotel_id, **data)    
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An error occurred updated the hotel.'}, 500
        return hotel.json(), 201
        

    def delete(self, hotel_id):
        hotel_located = HotelModel.find_hotel(hotel_id)
        if hotel_located:
            try:
                hotel_located.delete_hotel()
            except:
                return {'message': 'An error occurred deleting the hotel.'}, 500
            return {'message': 'Hotel deleted'}, 200
        return {'erro': f'hotel_id {hotel_id} nao encontrado'}, 404

