from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Book:')
    submit = SubmitField('Add Book')

class DelForm(FlaskForm):

    isbn = IntegerField('ISBN Number of Book to Remove:')
    submit = SubmitField('Remove Book')
