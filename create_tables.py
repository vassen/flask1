import sqlite3

quotes = [
    {
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
    },
    {
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
    },
    {
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы. На практике это не так."
    },

]
idx = 1
connection = sqlite3.connect('flask.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY,
    author NOT NULL,
    text TEXT NOT NULL,
    rating INTEGER DEFAULT 1
    )
    ''')
'''
try:
   cursor.execute('CREATE INDEX id_ ON quotes (id)')
except:
   pass
'''

try:
    for quote in quotes:
        cursor.execute('INSERT INTO quotes (id, author, text) VALUES (?, ?, ?)', (idx, quote["author"], quote["text"]))
        idx += 1
        print(idx)
        connection.commit()
except:
    pass

connection.close()
