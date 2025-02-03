from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, NumberRange, Length, EqualTo

class ApplicationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    school = StringField('Previous School', validators=[DataRequired()])
    gpa = FloatField('GPA', validators=[
        DataRequired(),
        NumberRange(min=0.0, max=10.0, message="GPA must be between 0.0 and 10.0")
    ])
    degree = StringField('Degree Applied For', validators=[DataRequired()])
    degree_document = FileField('Degree Certificate', validators=[DataRequired()])
    id_proof = FileField('ID Proof', validators=[DataRequired()])
    submit = SubmitField('Submit Application')

class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

class AdminSignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Admin')