from market import app
from flask import render_template
from market.models import Item
from market import db
from market.forms import RegisterForm

### Declare all routes here below ###


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['GET'])
def market_page():
    items = db.query(Item).all()
    db.close()
    return render_template('market.html', items=items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
