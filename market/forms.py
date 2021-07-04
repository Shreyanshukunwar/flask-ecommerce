from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from market.models import User

class RegisterForm(FlaskForm):

	def validate_username(self, username_to_check):
		user_check = username_to_check.data
		user = User.query.filter_by(username=user_check).first()
		if user is not None:
			raise ValidationError('Username already exists. Please use another Username')

	def validate_email_address(self, email_to_check):
		user = User.query.filter_by(email_address=email_to_check.data).first()
		if user is not None:
			raise ValidationError('Email already exists. Please use another.')

	username = StringField(label='Username', validators=[Length(min=2, max=20), DataRequired()])
	email_address = StringField(label='Email', validators=[Email(), DataRequired()])
	password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
	password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField(label='Register!')