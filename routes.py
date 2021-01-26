from app import app
from flask import request, jsonify
from models import Items
from sqlalchemy import func

@app.route('/', methods=['GET'])
def home():
    return '<p>API Homepage</p>'

@app.route('/api/blogs/all', methods=['GET'])
def position_all():
    all_items = Items.query.all()
    results = []
    for item in all_items:
        final = {}
        final['title'] = item.title
        final['body'] = item.body
        final['url'] = item.url
        results.append(final)
    return jsonify(results)

@app.route('/api/blog', methods=['GET'])
def position_filter():
    query_parameters = request.args
    id = query_parameters.get('id')
    title = query_parameters.get('title')

    filters = []
    if id:
        filters.append(Items.id == id)
    if title:
        filters.append(func.lower(Items.title) == title.lower())
    all_items = Items.query.filter(*filters).all()
    
    if filters == []:
        return page_not_found(404)
    results = []
    for item in all_items:
        final = {}
        final['id'] = item.id
        final['title'] = item.title
        final['body'] = item.body
        final['url'] = item.url
        results.append(final)
    return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404