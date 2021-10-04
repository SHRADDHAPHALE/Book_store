from books.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField 
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class AddForm(FlaskForm):

    name = StringField('Name of Book:')
    submit = SubmitField('Add Book')

class DelForm(FlaskForm):

    isbn = IntegerField('ISBN Number of Book to Remove:')
    submit = SubmitField('Remove Book')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')

