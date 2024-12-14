from flask import Flask
from flask import request
from flask import g
import sqlite3
import sql_work
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
import json



class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
BASE_DIR = Path(__file__).parent
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR / 'quote_alchemy.db'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)



class QuoteModel(db.Model):
    __tablename__ = 'quotes'

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(32))
    text: Mapped[str] = mapped_column(String(255))
    rating: Mapped[int]

    def __init__(self, author, text, rating):
        self.author = author
        self.text  = text
        self.rating = rating

@app.route("/quotes")
def quotes_all():
    data = sql_work.list_qoutes(db, QuoteModel)
    return data


@app.route("/quotes/<int:id>")
def quotes_(id):
    text = sql_work.get_quotes(db, QuoteModel, id)
    return text


@app.route("/quotes", methods=['POST'])
def create_quote():
    quote = request.json
    data = sql_work.create_quote(db, QuoteModel, quote)
    return data, 201


@app.route("/quotes/<int:id>", methods=['PUT'])
def update_quote(id):
    quote = request.json
    data = sql_work.update_quote(db, QuoteModel, id, quote)
    return data

@app.route("/quotes/<int:id>", methods=['DELETE'])
def delete(id):
    data = sql_work.delete_quote(db, QuoteModel, id)
    return data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
