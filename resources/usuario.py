from models.usuario import UserModel
from flask_restful import Resource, reqparse



class Usuarios(Resource):
    def get(self):
        return {'Usuarios': [user.json() for user in UserModel.query.all()]}


class Usuario(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('login', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank')

    def get(self, user_id):
        user_located = UserModel.find_user(user_id)
        if user_located:
            return user_located.json(), 200
        return {'message': 'Usuario não encontrado'}, 404

    def post(self, user_id):
        if UserModel.find_user(user_id):
            return {'message': 'Usuario já existe'}, 400
        
        data = Usuario.parser.parse_args()
        user = UserModel(user_id, **data)
        try:
            user.save_user()
        except:
            return {'message': 'Ocorreu um erro ao tentar cadastrar o usuário'}, 500
        return user.json(), 201
    
    def put(self, user_id):

        data = Usuario.parser.parse_args()

        user_located = UserModel.find_user(user_id)
        if user_located:
            user_located.update_user(**data)
            user_located.save_user()
            return user_located.json(), 200
        user = UserModel(user_id, **data)
        try:
            user.save_user()
        except:
            return {'message': 'Ocorreu um erro ao tentar cadastrar o usuário'}, 500
        return user.json(), 201

    def delete(self, user_id):
        user_located = UserModel.find_user(user_id)
        if user_located:
            try:
                user_located.delete_user()
            except:
                return {'message': 'Ocorreu um erro ao tentar deletar o usuário'}, 500
            return {'message': 'Usuario deletado'}, 200
        return {'message': 'Usuario não encontrado'}, 404
        