from app import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(200))
    body = db.Column(db.String(1000))

    def __repr__(self):
        return f"{self.title}, {self.url},{self.body}"