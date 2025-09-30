from App.database import db
from datetime import datetime

class Shift(db.Model):
    shiftId = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)

    def __init__(self, date, startTime, endTime):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        

    def assignStaff(self, staffId, shiftId=None): 
        return {
            'shiftId': shiftId,
            'date': self.date,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'assignedStaff': [staffId]
        }

    def get_json(self):
        return {
            'id': self.shiftId,
            'date': self.date,
            'startTime': self.startTime,
            'endTime': self.endTime
        }
