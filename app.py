from flask import Flask
from flask import request
from flask import g
import sqlite3
import sql_work
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATABASE = BASE_DIR / "flask.db"  


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE,autocommit=True)
    return db

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
   return "Hello, World!"

@app.route("/quotes")
def quotes_all():
    cursor = get_db().cursor()
    data = sql_work.list_qoutes(cursor)
    return data

@app.route("/quotes/<int:id>")
def quotes_(id):
    cursor = get_db().cursor()
    text = sql_work.get_quotes(cursor,id)
    return text

@app.route("/quotes", methods=['POST'])
def create_quote():
   cursor = get_db().cursor()
   quote = request.json
   sql_work.create_quote(cursor,quote)
   return quote, 201

@app.route("/quotes/<int:id>", methods=['PUT'])
def update_quote(id):
   cursor = get_db().cursor()
   quote = request.json
   data = sql_work.update_quote(connection,cursor,quote,id)
   return data

@app.route("/quotes/count")
def count_quote():
   cursor = get_db().cursor()
   lenght = sql_work.count_quotes(cursor)
   count={"count":lenght}
   return count

@app.route("/quotes/random")
def random():
   cursor = get_db().cursor()
   data = sql_work.random_quote(cursor)
   print("data",data)
   return data

@app.route("/quotes/<int:id>", methods=['DELETE'])
def delete(id):
   cursor = get_db().cursor()
   data = sql_work.delete_quote(cursor,id)
   return data

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')
