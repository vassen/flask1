import random

def list_qoutes(cursor):
   quotes=""
   cursor.execute('SELECT * FROM quotes')
   data = cursor.fetchall()
   for quote in data:
     quotes += str(quote)
     quotes += "</br>"
   return quotes

def random_quote(cursor):
   ids=[]
   cursor.execute('SELECT id FROM quotes')
   data = cursor.fetchall()
   for id in data:
       ids.append(id[0])
   id = random.choice(ids)
   cursor.execute('SELECT text FROM quotes WHERE id = ?', (id,))
   data = cursor.fetchall()[0][0]
   return data


def get_quotes(cursor,id):
   try:
      cursor.execute(f'SELECT text FROM quotes where id={id}')
      data = cursor.fetchone()
      return data[0]
   except:
      return f"Quote with id={id} not found", 404

def create_quote(cursor,quote):
   if quote.get("rating")==None or quote["rating"]>5 or quote["rating"]<1:
       quote["rating"]=1
   cursor.execute('SELECT max(id) FROM quotes')
   last_id = cursor.fetchone()[0]+1
   cursor.execute('INSERT INTO quotes (id, author, text, rating) VALUES (?, ?, ?, ?)', (last_id,str(quote["author"]),str(quote["text"]),str(quote["rating"])))

def count_quotes(cursor): 
   cursor.execute('SELECT count(id) FROM quotes')
   data = cursor.fetchone()
   return data


def update_quote(connection,cursor,new_quote,id):
   sql_quote={}
   cursor.execute('SELECT * FROM quotes where id=?',(id,))
   data = cursor.fetchall()[0]
   if  new_quote["rating"]>5 or new_quote["rating"]<1:
       new_quote.pop("rating")
   sql_quote["author"]=data[1]
   sql_quote["text"]=data[2]
   sql_quote["rating"]=data[3]
   sql_quote.update(new_quote)
   cursor.execute('UPDATE quotes set author = ?,text =?, rating = ? where id=? ', (str(sql_quote["author"]),str(sql_quote["text"]), sql_quote["rating"],id))
   return sql_quote, 200

   return f"Quote with id={id} not found", 404

def delete_quote(cursor,id):
   cursor.execute('DELETE FROM quotes WHERE id = ?', (id,))
   row = cursor.rowcount
   if not cursor.rowcount==0:
       return f"Quote with id {id} is deleted.", 200
   else:
       return f"Quote with id {id} not found", 200

