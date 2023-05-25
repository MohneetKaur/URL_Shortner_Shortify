from flask import Flask, render_template, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import string
import random

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__)) # returns the absolute i.e. whole path for proj_7
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class URL(db.Model):
    __tablename__ = 'URL_Comparison'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), nullable=False, unique=True)

    def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_code = short_url

    def __repr__(self):
        return f'<URL {self.original_url} ({self.short_code})>'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        url = URL(original_url,short_code)
        db.session.add(url)
        db.session.commit()
        short_url = request.host_url + short_code
        return render_template('home.html', short_url=short_url)
    return render_template('home.html')

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for i in range(6))
    if URL.query.filter_by(short_code=short_code).first():
        return generate_short_code()
    return short_code

@app.route('/history')
def history():
    urls = URL.query.all()
    return render_template('history.html', urls=urls)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    app.run(debug=True)
