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
   print(id)
   cursor.execute('SELECT text FROM quotes WHERE id = ?', (id,))
   data = cursor.fetchall()[0][0]
   return data



def get_quotes(cursor,id):
   try:
      cursor.execute(f'SELECT text FROM quotes where id={id}')
      data = cursor.fetchall()
      return data[0][0]
   except:
      return f"Quote with id={id} not found", 404

def create_quote(connection,cursor,quote):
   print(type(quote))
   if quote.get("rating")==None or quote["rating"]>5 or quote["rating"]<1:
       quote["rating"]=1
   cursor.execute('SELECT max(id) FROM quotes')
   last_id = cursor.fetchall()[0][0]+1
   cursor.execute('INSERT INTO quotes (id, author, text, rating) VALUES (?, ?, ?, ?)', (last_id,str(quote["author"]),str(quote["text"]),str(quote["rating"])))
   connection.commit()
   print("data", quote)

def count_quotes(cursor): 
   cursor.execute('SELECT id FROM quotes')
   data = cursor.fetchall()
   count = len(data)
   print(count)
   return count


def update_quote(connection,cursor,new_quote,id):
    try:
      sql_quote={}
      cursor.execute(f'SELECT * FROM quotes where id={id}')
      data = cursor.fetchall()[0]
      print(data)
      sql_quote["author"]=data[1]
      sql_quote["text"]=data[2]
      sql_quote.update(new_quote)
      cursor.execute('UPDATE quotes set author = ?,text =? where id=? ', (str(sql_quote["author"]),str(sql_quote["text"]),id))
      return sql_quote, 200
    except:
      return f"Quote with id={id} not found", 404

def delete_quote(connection,cursor,id):
   cursor.execute('SELECT id FROM quotes WHERE id = ?',(id,))
   row = cursor.rowcount
   data = cursor.fetchall()
   print("data",data)
   if not data:
      return f"Quote with id={id} not found", 404
   else:
      cursor.execute('DELETE FROM quotes WHERE id = ?', (id,))
      connection.commit()
      return f"Quote with id {id} is deleted.", 200

