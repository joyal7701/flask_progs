from flask import render_template, redirect, Flask, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
blueprint = make_google_blueprint(
    client_id='', client_secret='', offline=True, scope=['profile', 'emial'])
app.register_blueprint(blueprint, url_prefix='/login')
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)


@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)
