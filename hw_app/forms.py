from flask_wtf import FlaskForm
from marshmallow import ValidationError
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserSignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    age = IntegerField('Age')
    submit_button = SubmitField()

    def validate_age(form, field):
        if field.data < 18:
            raise ValidationError('You must be 18 years or older to purchase a car.')

class UserSignInForm(FlaskForm):
    # email, password, submit
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()