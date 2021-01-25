from position_scrape import scrape
from flask import jsonify
from models import db, Items

def reset_data():
    db.drop_all()
    db.create_all()

def write_data():
    items = scrape('https://mightyhive.com', '/current-openings')
    exist_items = Items.query.all()
    exist_urls = []
    for exist_item in exist_items:
        exist_urls.append(exist_item.url)

    for item in items:
        department = item['department']
        office = item['office']
        position = item['position']
        url = item['url']
        if url in exist_urls:
            pass
        else:
            item_to_put = Items(
                department = department, 
                office = office, 
                position = position, 
                url = url)

            db.session.add(item_to_put)
            db.session.commit()