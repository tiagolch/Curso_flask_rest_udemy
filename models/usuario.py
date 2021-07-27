from flask_sqlalchemy import SQLAlchemy

class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)


    def __init__(self, user_id, login, password):
        self.user_id = user_id
        self.login = login
        self.password = password

    def json(self):
        return {
            'user_id': self.user_id, 
            'login': self.login
        }


    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self, login, password):
        self.login = login
        self.password = password
  
    def delete_hotel(self):
        db.session.delete(self)
        db.session.commit()
