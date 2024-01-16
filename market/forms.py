from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, Optional, ValidationError
from market import db
from market.models import Item, User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        print(username_to_check.data)
        user = db.query(User).filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist!')

    username = StringField(
        label='User Name:',
        validators=[
            Length(min=4, max=8, message="User Name character must be between 4 to 8"),
            DataRequired(message="User Name required")
        ]
    )
    email_address = StringField(
        label='Email Address:',
        validators=[
            Email("Invalid Email Address")
        ]
    )
    password1 = PasswordField(
        label='Password:',
        validators=[
            Length(min=8, max=12, message="Password character must be between 8 to 12"),
            DataRequired(message="Password required")
        ]
    )
    password2 = PasswordField(
        label='Confirm Password:',
        validators=[
            EqualTo('password1', message="Confirmation of password does not match")
        ]
    )

    submit = SubmitField(label='submit')
