import flask
from flask import request, jsonify
from books import books

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>API Homepage</h1>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []
    for book in books:
        if book['id'] ==id:
            results.append(book)

    return jsonify(results)

app.run()
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals