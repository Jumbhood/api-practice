from blog_scrape import scrape
from flask import jsonify
from models import db, Items

def reset_data():
    db.drop_all()
    db.create_all()

def write_data():
    items = scrape('https://blog.certn.co', '/certn-blog-2020')
    exist_items = Items.query.all()
    exist_urls = []
    for exist_item in exist_items:
        exist_urls.append(exist_item.url)

    for item in items:
        title = item['title']
        body = item['body']
        url = item['url']
        if url in exist_urls:
            pass
        else:
            item_to_put = Items(
                title = title, 
                body = body, 
                url = url)

            db.session.add(item_to_put)
            db.session.commit()