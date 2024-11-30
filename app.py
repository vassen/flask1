from flask import Flask
from random import choice
from flask import request
import sqlite3
import sql_work
connection = sqlite3.connect('flask.db',check_same_thread=False)
cursor = connection.cursor()


app = Flask(__name__)
quotes = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
   },
   {
       "id": 6,
       "author": "Mosher’s Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так."
   },

]
'''quote_id=[]
for quote in quotes:
   quote_id.append(quote["id"])
'''
#app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
   return "Hello, World!"


@app.route("/quotes/<int:id>")
def quotes_html(id):
      text = sql_work.get_quotes(cursor,id)
      return text

@app.route("/quotes", methods=['POST'])
def create_quote_html():
   quote = request.json
   sql_work.create_quote(connection,cursor,quote)
   print("data", quote)
   return {}, 201

'''@app.route("/quotes", methods=['PUT'])
def create_quote():
   data = request.json
   print("data", data)
   return {}, 201'''

@app.route("/count")
def count_html():
   cursor.execute('SELECT max(id) FROM quotes')
   last_id = cursor.fetchall()
   lenght = last_id[0][0]
   count={"count":lenght}
   return count

@app.route("/random")
def random():
   id=choice(quote_id)
   for quote in quotes:
      if quote["id"]==id:
        return quote["text"]

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')
