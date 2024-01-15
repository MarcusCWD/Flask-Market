from flask import Flask, render_template, request, jsonify
from sqlalchemy.orm import Session
from model import engine, Base, Item
import os

app = Flask(__name__)

# Create the database tables (SERIOUSLY. REMEMBER TO DELETE)
Base.metadata.create_all(bind=engine)

# Create a SQLAlchemy session
db = Session(bind=engine)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['GET'])
def market_page():
    items = db.query(Item).all()
    # item_list = [{'id': item.id,
    #               'name': item.name,
    #               'price': item.price,
    #               'barcode': item.barcode,
    #               'description': item.barcode
    #               } for item in items]
    # item_list = [{key: value for key, value in item.__dict__.items() if not key.startswith('_')}
    #               for item in items]
    db.close()
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('APP_PORT'))
