import random


def list_qoutes(db,QuoteModel):
    quotes = ""
    quote_all =db.session.scalars(db.select(QuoteModel)).all()
    for quote in quote_all:
        print(quote.author)
        quotes += f"id = {quote.id}, author = {quote.author}, text= {quote.text}"
        quotes += "</br>"
    return quotes



def get_quotes(db,QuoteModel,id):
    data = db.session.get(QuoteModel, id)
    if data is not None:
        return data.text
    else:
        return f"Quote with id={id} not found", 404


def create_quote(db,QuoteModel,quote_post):
    if quote_post.get("rating") == None or quote_post["rating"] is not range(1,6):
        quote_post["rating"] = 1
    print(quote_post)
    quote = QuoteModel(quote_post['author'],quote_post['text'],quote_post['rating'])
    db.session.add(quote)
    db.session.commit()
    id = str(quote.id)
    return f"add quote id = {id},</br>quotes = </br>{quote_post}"


def update_quote(db, QuoteModel, id, quote):
    data = db.session.get(QuoteModel, id)
    if data is not None:
        q = db.session.get(QuoteModel, id)
        print(q.id)
        try:
            if quote['author'] is not None:
                q.author = quote['author']
        except:
            pass

        try:
            if quote['text'] is not None:
                q.text = quote['text']
        except:
            pass
        try:
            if quote['rating'] is not None or quote['rating'] not in range(1,6):
                q.text = quote['text']
        except:
            pass
        db.session.add(q)
        db.session.commit()
    
        return str(quote) + "</br> Edit completed", 200
    else:
        return f"id = {id} Not found", 200


def delete_quote(db, QuoteModel, id):
    data = db.session.get(QuoteModel, id)
    if data is not None:
        db.session.delete(data)
        db.session.commit()
        return f"Quote with id {id} is deleted.", 200
    else:
        return f"Quote with id={id} not found", 404

