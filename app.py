import flask
from flask import request, jsonify
import sqlite3
from books import books
from coffees import coffees

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>API Homepage</h1>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def book_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute("SELECT * FROM books;").fetchall()
    return jsonify(all_books)

@app.route('/api/v1/resources/books', methods=['GET'])
def book_filter():
    query_parameters = request.args
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query = query + " id=? AND"
        to_filter.append(id)
    if published:
        query = query + " published=? AND"
        to_filter.append(published)
    if author:
        query = query + " author=? AND"
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ";"
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/api/v1/resources/coffees/all', methods=['GET'])
def coffee_all():
    return jsonify(coffees)

@app.route('/api/v1/resources/coffee', methods=['GET'])
def coffee_id():
    # Check if an ID is provided as part of the URL
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    # Create a empty result list to store the data
    results = []

    #according to ID from the URL, find the book in 
    for coffee in coffees:
        if coffee['id'] == id:
            results.append(coffee)

    return jsonify(results)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run()
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals