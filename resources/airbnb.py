from flask_restful import Resource, reqparse
from models.airbnb import AirbnbModel


class AirbnbList(Resource):
    def get(self):
        return {'airbnb': [airbnb.json() for airbnb in AirbnbModel.query.all()]}


class Airbnb(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('city')
    parser.add_argument('state')
    parser.add_argument('country')
    parser.add_argument('price')
    


    def get(self, airbnb_id):
        airbnb_located = AirbnbModel.find_airbnb(airbnb_id)  
        if airbnb_located:
            return airbnb_located.json(), 200
        return {'message': 'Airbnb not found'}, 404      

    def post(self, airbnb_id):
        if AirbnbModel.find_airbnb(airbnb_id):
            return {'message': f'Airbnb {airbnb_id} already exists'}, 400

        data = Airbnb.parser.parse_args()       
        airbnb = AirbnbModel(airbnb_id, **data)
        try:
            airbnb.save_airbnb()
        except:
            return {'message': 'An error occurred inserting the airbnb'}, 500
        return airbnb.json(), 201
        

    def put(self, airbnb_id):

        data = Airbnb.parser.parse_args()

        airbnb_located =  AirbnbModel.find_airbnb(airbnb_id)
        if airbnb_located:
            airbnb_located.update_airbnb(**data)
            airbnb_located.save_airbnb()
            return airbnb_located.json(), 200
        airbnb = AirbnbModel(airbnb_id, **data)
        try:
            airbnb.save_airbnb()
        except:
            return {'message': 'An error occurred inserting the airbnb'}, 500
        return airbnb.json(), 201


    def delete(self, airbnb_id):
        airbnb_located = AirbnbModel.find_airbnb(airbnb_id)
        if airbnb_located:
            try:
                airbnb_located.delete_airbnb()
            except:
                return {'message': 'An error occurred deleting the airbnb'}, 500
            return {'message': 'Airbnb deleted'}, 200
        return {'message': 'Airbnb not found'}, 404

