from flask_restful import Resource, reqparse
from models.airbnb import AirbnbModel


airbnb = [
    {
        'airbnb_id':'casa1', 
        'city':'Rio de Janeiro', 
        'state':'RJ', 
        'country':'Brasil',
        'price':120
    },
]


class AirbnbList(Resource):
    def get(self):
        return {'airbnb': airbnb}


class Airbnb(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('city')
    parser.add_argument('state')
    parser.add_argument('country')
    parser.add_argument('price')
    
    def find_airbnb(self, airbnb_id):
        for air in airbnb:
            if air['airbnb_id'] == airbnb_id:
                return air
        return None


    def get(self, airbnb_id):
        airbnb = Airbnb.find_airbnb(airbnb_id)  
        if airbnb:
            return airbnb
        return {'message': 'Airbnb not found'}, 404      

    def post(self, airbnb_id):
        data = Airbnb.parser.parse_args()

        for air in airbnb:
            if airbnb_id == air['airbnb_id']:
                return {'message': f'Airbnb {airbnb_id} already exists'}, 400

        object_airbnb = AirbnbModel(airbnb_id, **data)
        new_airbnb = object_airbnb.json()

        airbnb.append(new_airbnb)
        return {'airbnb': airbnb}, 200
        

    def put(self, airbnb_id):
        data = Airbnb.parser.parse_args()

        object_airbnb = AirbnbModel(airbnb_id, **data)
        updated_airbnb = object_airbnb.json()

        airbnb =  Airbnb.find_airbnb(airbnb_id)

        if airbnb:
            airbnb.update(updated_airbnb)
            return updated_airbnb, 200
        airbnb.append(updated_airbnb)
        return updated_airbnb, 201


    def delete(self, airbnb_id):
        air = Airbnb.find_airbnb(airbnb_id)
        if air:
            airbnb.remove(airbnb)
            return {'message': f'Airbnb {airbnb_id} deleted'}, 200
        return {'message': f'Airbnb {airbnb_id} not found'}, 404










