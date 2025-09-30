from App.database import db
from datetime import datetime

class Staff(db.Model):
    staffId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(100), nullable=False)


    def get_json(self):
        return {
            'id': self.staffId,
            'username': self.username,
            'position': self.position,
        }

    def time_in(self):
        self.time_in = datetime.now()
        db.session.commit()

    def time_out(self):
        self.time_out = datetime.now()
        db.session.commit()

    def viewRoster(self, rosterId):
        return{
            'rosterId': rosterId,
            'shifts': [],
            'staffId': [self.staffId]
        }
