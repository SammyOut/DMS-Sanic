from datetime import datetime
from typing import Any

from const import EXTENSION_CLASS, EXTENSION_TIME, GOINGOUT_STATUS, MUSIC_APPLY_WEEKDAY, STAY_STATUS
from extension import db
from utils import kst_now


class BaseApplyModel(db.Model):
    __abstract__ = True

    id: int = db.Column(db.Integer(), primary_key=True)
    student_id: str = db.Column(db.String, db.ForeignKey('student.username', ondelete='CASCADE'))
    apply_date = db.Column(db.DateTime(), default=kst_now)

    @classmethod
    async def query_by_id(cls, id: Any):
        return await cls.query.where(cls.id == id).gino.first()

    @classmethod
    async def query_by_student(cls, student_id: str):
        return await cls.query.where(cls.student_id == student_id).gino.first()


class ExtensionApplyModel(BaseApplyModel):
    __tablename__ = 'apply_extension'

    time: int = db.Column(db.Enum(EXTENSION_TIME))
    class_: int = db.Column(db.Enum(EXTENSION_CLASS))
    seat: int = db.Column(db.Integer())


class GoingoutApplyModel(BaseApplyModel):
    __tablename__ = 'apply_goingout'

    go_out_date: datetime = db.Column(db.DateTime())
    come_back_date: datetime = db.Column(db.DateTime())
    reason: str = db.Column(db.String())
    status: str = db.Column(db.Enum(GOINGOUT_STATUS))


class MusicApplyModel(BaseApplyModel):
    __tablename__ = 'apply_music'

    day: int = db.Column(db.Enum(MUSIC_APPLY_WEEKDAY))
    singer: str = db.Column(db.String())
    song_name: str = db.Column(db.String())


class StayApplyModel(BaseApplyModel):
    __tablename__ = 'apply_stay'

    status: int = db.Column(db.Enum(STAY_STATUS))
