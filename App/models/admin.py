from App.database import db

class Admin(db.Model):
    adminId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def get_json(self):
        return {
            'id': self.adminId,
            'username': self.username,
        }
    
    def scheduleShift(self, shiftId, date, startTime, endTime):
        return {
            'shiftId': shiftId,
            'date': date,
            'startTime': startTime,
            'endTime': endTime
        }
