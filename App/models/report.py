from App.database import db

class Report(db.Model):
    reportId = db.Column(db.Integer, primary_key=True)
    rosterId = db.Column(db.Integer, db.ForeignKey('roster.rosterId'), nullable=False)
    staffId = db.Column(db.Integer, db.ForeignKey('staff.staffId'), nullable=False)
    roster = db.relationship('Roster')
    staff = db.relationship('Staff')

    def init(self, rosterId, staffId):
        self.rosterId = rosterId
        self.staffId = staffId

    def viewReport(self):
        return {
            'id': self.reportId,
            'roster_id': self.rosterId,
            'staff_id': self.staffId
        }
