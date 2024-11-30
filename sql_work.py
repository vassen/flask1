def get_quotes(cursor,id):
   try:
      cursor.execute(f'SELECT text FROM quotes where id={id}')
      text = cursor.fetchall()
      return text[0][0]
   except:
      return f"Quote with id={id} not found", 404

def create_quote(connection,cursor,quote):
   print(quote)
   cursor.execute('SELECT max(id) FROM quotes')
   last_id = cursor.fetchall()[0][0]+1
   cursor.execute('INSERT INTO quotes (id, author, text) VALUES (?, ?, ?)', (last_id,str(quote["author"]),str(quote["text"])))
   connection.commit()
   print("data", quote)

def count_html():
   cursor.execute('SELECT max(id) FROM quotes')
   last_id = cursor.fetchall()
   lenght = last_id[0][0]
   count={"count":lenght}
