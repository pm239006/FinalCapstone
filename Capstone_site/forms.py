from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DecimalField
from wtforms.validators import DataRequired, EqualTo, Email



#create our login form
class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

#create our register form

class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[ DataRequired() ])
    email = StringField('Email', validators=[ DataRequired(), Email() ])
    password = PasswordField('Password', validators = [ DataRequired()])
    verify_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# create our pet form

class PetForm(FlaskForm):
    pet_name = StringField("Pet Name", validators=[ DataRequired()])
    age = StringField("Age")
    birthday = StringField("Birthday")
    image = StringField("ImageUrl")
    breed = StringField("Breed")
    fur_color = StringField("Fur Color")
    gender = StringField("Gender")
    home_trained = BooleanField("Home trained?")
    submit = SubmitField('Add Pup') 

