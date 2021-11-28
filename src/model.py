from config import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.label

    def __init__(self, label, status=0):
        self.label = label
        self.status = status

    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "status": self.status
        }
