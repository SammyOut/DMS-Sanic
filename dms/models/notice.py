from datetime import datetime

from extension import db
from utils import kst_now


class BaseNoticeModel(db.Model):
    __abstract__ = True

    id: int = db.Column(db.Integer(), primary_key=True)
    post_date: datetime = db.Column(db.DateTime(), default=kst_now)
    title: str = db.Column(db.String())
    content: str = db.Column(db.String())


class NoticeModel(db.Model):
    pass


class RuleModel(db.Model):
    pass
