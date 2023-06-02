from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import InputRequired

class PLL_Address_Book(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phone_number = StringField('Phone Number', validators=[InputRequired()])
    address = StringField('Address')
    submit = SubmitField('PLL Address Book')

class Home(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    submit = SubmitField('Home')