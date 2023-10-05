from werkzeug.security import generate_password_hash 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, LoginManager, current_user 
from datetime import datetime
import uuid 
from flask_marshmallow import Marshmallow
from .helpers import get_image
db = SQLAlchemy() 
login_manager = LoginManager() 
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    user_id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(30),unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    pet = db.relationship('Pet', backref = 'owner', lazy = True)

    def __init__(self,username,email,password, first_name= "", last_name = ""):
        self.user_id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_id(self):
        return str(uuid.uuid4())
    def get_id(self):
        return str(self.user_id)

    def set_password(self,password):
        return generate_password_hash(password)
    
    def __repr__(self):
        return f"USER: {self.username}"

class Pet(db.Model):
    pet_id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.String(4))
    birthday = db.Column(db.DateTime)
    image = db.Column(db.String(500))  
    breed = db.Column(db.String(100))
    birthday = db.Column(db.DateTime)
    fur_color = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    home_trained = db.Column(db.Boolean)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable = False) #if we wanted to make a foreign key relationship


    def __init__(self, name, age, birthday, breed, fur_color, gender, home_trained,image = ""):
        self.pet_id = self.set_id()
        self.name = name
        self.age = age
        self.birthday = birthday
        self.image = set.self_image(self,breed)
        self.breed = breed
        self.fur_color = fur_color
        self.gender = gender
        self.home_trained = home_trained
        self.user_id = current_user.user_id
      

    def set_id(self):
        return str(uuid.uuid4()) #create unique ID 
    
    def set_image(self,image,breed):
        if not image: 
            image = get_image(breed)
        return image
 
    def __repr__(self):
        return f"<PET: {self.name}>"


class PetSchema(ma.Schema):
    class Meta: 
        fields = ['name', 'age', 'birthday', 'image', 'breed', 'fur_color', 'gender', 'home_trained'] 



pet_schema = PetSchema() 
pets_schema = PetSchema(many = True) 
    
