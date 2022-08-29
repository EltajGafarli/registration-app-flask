from app import db
from app import bcrypt
from app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(50),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(500),nullable=False)    
    def __init__(self,username,email,password):
        self.username = username 
        self.email = email
        self.password_hash = password
    def __repr__(self):
        return {
            "data":[
                self.username,self.email
            ]
        }
    
    @property
    def password_hash(self):
        return self.password
    
    @password_hash.setter
    def password_hash(self,password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    @classmethod
    def get_all_users(cls):
        users = cls.query.all()
        return users
    @classmethod
    def add_user(cls,username,email,password):
        user = cls(username,email,password)
        db.session.add(user)
        db.session.commit()
        
        
    def check_user(self,password):
        
        return bcrypt.check_password_hash(self.password_hash,password)
    
    
