from App.database import db
from datetime import datetime

class Roster(db.Model):
    rosterId = db.Column(db.Integer, primary_key=True)
    staffId = db.Column(db.Integer, db.ForeignKey('staff.staffId'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time_in = db.Column(db.DateTime, nullable=False)
    time_out = db.Column(db.DateTime, nullable=False)

    def init(self, staffId, date, time_in, time_out):
        self.staffId = [staffId]
        self.date = date
        self.time_in = time_in
        self.time_out = time_out

    def get_json(self):
        return {
            'id': self.rosterId,
            'staff_id': self.staffId,
            'date': self.date,
            'time_in': self.time_in,
            'time_out': self.time_out
        }
