from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30) , nullable=False, unique=True)
    price = db.Column(db.int() , nullable=False)
    name = db.Column(db.String(length=12) , nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')




@app.route("/market")
def market_page():
    items = [{'id': 1, 'name': 'phone', 'barcode': '08192221', 'price': 500},
             {'id': 2, 'name': 'laptop', 'barcode': '08132222', 'price': 900},
             {'id': 3, 'name': 'keyboard', 'barcode': '08492223', 'price': 150}]

    return render_template('market.html', items = items)

