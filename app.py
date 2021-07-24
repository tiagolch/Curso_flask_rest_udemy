from resources.hotel import Hoteis, Hotel
from resources.airbnb import Airbnb, AirbnbList
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis, '/hoteis')
api.add_resource(AirbnbList, '/airbnbList')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Airbnb, '/airbnb/<string:airbnb_id>')




if __name__ == '__main__':
    app.run(debug=True)
