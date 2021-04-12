from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
class Addform(FlaskForm):
    name=StringField('name of puppy: ')
    submit=SubmitField('add puppy')
class Delform(FlaskForm):
    id=IntegerField("id number of puppy to remove: ")
    submit=SubmitField('remove puppy')
class Addowner(FlaskForm):
    name=StringField('name of owner: ')
    pup_id=IntegerField("ID of puppy: ")
    submit=SubmitField("Add owner")
