####################
## Import statements
####################

from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, PasswordField
from wtforms.validators import Required, Length, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'
app.debug = True

########################
##### Set up Form #####
########################


class RegistrationForm(FlaskForm):
	
	firstName = StringField('First Name:', validators=[Required(),Length(1,64)])
	lastName = StringField('Last Name:', validators=[Required(),Length(1,64)])
	email = StringField('Email:', validators=[Required(),Length(1,64),Email()])
	password = PasswordField('Password:',validators=[Required(),EqualTo('password2',message="Passwords must match")])
	password2 = PasswordField("Confirm Password:",validators=[Required()])
	submit = SubmitField('Register')
	
	


@app.route('/', methods=['GET', 'POST'])
def index():
	form = RegistrationForm()
	
	return render_template('base.html', form = form)
	
	


if __name__ == '__main__':
	
	app.run(use_reloader=True,debug=True) 




