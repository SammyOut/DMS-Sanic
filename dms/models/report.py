from extension import db


class FacilityReportModel(db.Model):
    __tablename__ = 'facility_report'

    id: int = db.Column(db.Integer(), primary_key=True)
    student_id: str = db.Column(db.String(), db.ForeignKey('student.username', ondelete='CASCADE'))
    room_number: int = db.Column(db.Integer())
    content: str = db.Column(db.String())
