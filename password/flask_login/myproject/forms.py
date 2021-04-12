from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


class loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('log in')


class registrationform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='passwords must match!')])
    pass_confirm = PasswordField(
        'confirm password', validators=[DataRequired()])
    submit = SubmitField('register!')

    def check_email(self, field):
        if user.query.filter_by(email=field.data).first():
            raise ValidationError('your email has been already register')

    def check_username(self, field):
        if user.query.filter_by(username=field.data).first():
            raise ValidationError('username is taken!')
