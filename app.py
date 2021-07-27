from resources.hotel import Hoteis, Hotel
from resources.airbnb import Airbnb, AirbnbList
from resources.usuario import Usuario, Usuarios
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    db.create_all()


api.add_resource(Hoteis, '/hoteis')
api.add_resource(AirbnbList, '/airbnbList')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Airbnb, '/airbnb/<string:airbnb_id>')
api.add_resource(Usuarios, '/users')
api.add_resource(Usuario, '/user/<int:user_id>')




if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
