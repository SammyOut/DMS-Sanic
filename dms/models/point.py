from datetime import datetime

from extension import db


class PointItemModel(db.Model):
    __tablename__ = 'point_item'

    id: int = db.Column(db.Integer(), primary_key=True)
    reason: str = db.Column(db.String())
    point: int = db.Column(db.Integer())
    type: bool = db.Column(db.Boolean())


class PointHistoryModel(db.Model):
    __tablename__ = 'point_history'

    id: int = db.Column(db.Integer(), primary_key=True)
    student_id: str = db.Column(db.String(), db.ForeignKey('student.username', ondelete='CASCADE'))
    point_id: int = db.Column(db.Integer(), db.ForeignKey('point_item.id', ondelete='CASCADE'))
    point_date: datetime = db.Column(db.DateTime())


class PointStatusModel(db.Model):
    __tablename__ = 'point_status'

    student_id: str = db.Column(db.String(), db.ForeignKey('student.username', ondelete='CASCADE'), primary_key=True)
    good_point: int = db.Column(db.Integer())
    bad_point: int = db.Column(db.Integer())
    penalty_level: int = db.Column(db.Integer())
    penalty_status: bool = db.Column(db.Boolean())
