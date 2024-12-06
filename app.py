from flask import Flask
from flask import request
import sqlite3
import sql_work

connection = sqlite3.connect('flask.db',check_same_thread=False)
cursor = connection.cursor()
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
   return "Hello, World!"

@app.route("/quotes")
def quotes_all():
    data = sql_work.list_qoutes(cursor)
    return data

@app.route("/quotes/<int:id>")
def quotes_(id):
      text = sql_work.get_quotes(cursor,id)
      return text

@app.route("/quotes", methods=['POST'])
def create_quote():
   quote = request.json
   sql_work.create_quote(connection,cursor,quote)
   return quote, 201

@app.route("/quotes/<int:id>", methods=['PUT'])
def update_quote(id):
   quote = request.json
   data = sql_work.update_quote(connection,cursor,quote,id)
   return data

@app.route("/quotes/count")
def count_quote():
   lenght = sql_work.count_quotes(cursor)
   count={"count":lenght}
   return count

@app.route("/quotes/random")
def random():
   data = sql_work.random_quote(cursor)
   print("data",data)
   return data

@app.route("/quotes/<int:id>", methods=['DELETE'])
def delete(id):
   data = sql_work.delete_quote(connection,cursor,id)
   return data

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')
