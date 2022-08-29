from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import DateField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms.validators import Email,EqualTo,Length,DataRequired,ValidationError

from app.models import Users

class SignUpForm(FlaskForm):
    
    def validate_username(self,username_to_check):
        user = Users.query.filter_by(username = username_to_check.data).first()
        
        if user:
            raise ValidationError('Username already exist.')
    
    def validate_email(self,email_to_check):
        email_adress = Users.query.filter_by(email = email_to_check.data).first()
        
        if email_adress:
            raise ValidationError('Email already exist.')
    
    username = StringField(label='username',validators=[DataRequired(),Length(min = 3)])
    email = StringField(label='email',validators=[Length(min=11),Email(),DataRequired()])
    password1 = PasswordField(label='password1',validators=[Length(min=5),DataRequired()])
    password2 = PasswordField(label='password2',validators=[Length(min=5),DataRequired(),EqualTo('password1')])
    submit = SubmitField(label='submit')
class LoginForm(FlaskForm):
    username = StringField(label='username',validators=[DataRequired()])
    password = PasswordField(label='password1',validators=[DataRequired()])
    submit = SubmitField(label='submit')