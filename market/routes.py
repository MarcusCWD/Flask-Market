from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
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


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.add(user_to_create)
        db.commit()
        return redirect(url_for('market_page'))
    # if there are any error in the form
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg[0]}')

    return render_template('register.html', form=form)
