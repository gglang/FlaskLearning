from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Gerald'}
	posts = [
		{
			'author': {'username': 'Micky'},
			'body': 'Herka derka mcderka'
		},
		{
			'author': {'username': 'Annie'},
			'body': 'Meowy meow meow meow'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)