import random
import json

def list_qoutes(db,QuoteModel):
    quotes = {}
    q = {}
    quote_all = db.session.scalars(db.select(QuoteModel)).all()
    for quote in quote_all:
        q['id']=quote.id
        q['author']=quote.author
        q['text']=quote.text
        q['ratind']=quote.rating
        quotes.append(q)
    if quotes=={}:
       quotes["error"] = "quotes is empty"
       print(quotes)
       return quotes
    return quotes



def get_quotes(db,QuoteModel,id):
    result = {}
    data = db.session.get(QuoteModel, id)
    if data is not None:
        result['text'] = data.text
        return result
    else:
        result['error'] = f"id not found"
        result['id'] = id
        return result, 404


def create_quote(db,QuoteModel,quote_post):
    if quote_post.get("rating") == None or quote_post["rating"] is not range(1,6):
        quote_post["rating"] = 1
    print(quote_post)
    quote = QuoteModel(quote_post['author'],quote_post['text'],quote_post['rating'])
    db.session.add(quote)
    db.session.commit()
    quote_post['id'] = quote.id
    return quote_post


def update_quote(db, QuoteModel, id, quote):
    data = db.session.get(QuoteModel, id)
    if data is not None:
        try:
            if quote['author'] is not None:
                data.author = quote['author']
        except:
            pass

        try:
            if quote['text'] is not None:
                data.text = quote['text']
        except:
            pass
        try:
            if quote['rating'] is not None or quote['rating'] not in range(1,6):
                data.text = quote['text']
        except:
            pass
        db.session.add(data)
        db.session.commit()
        #quote['error'] = "quote update"
        return quote, 200
    else:
        quote['error'] = f"id {id} Not found"
        return quote, 404


def delete_quote(db, QuoteModel, id):
    result = {}
    data = db.session.get(QuoteModel, id)
    if data is not None:
        db.session.delete(data)
        db.session.commit()
        result['status']= f"Quote with id {id} is deleted."
        return result
    else:
        result['status']= f"Quote with id={id} not found"
        return result, 404

