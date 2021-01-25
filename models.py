from app import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    department = db.Column(db.String(100))
    office = db.Column(db.String(100))
    position = db.Column(db.String(100))
    url = db.Column(db.String(300))

    def __repr__(self):
        return f"{self.department}, {self.office},{self.position},{self.url}"