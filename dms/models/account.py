from uuid import uuid4

from extension import db


class BaseStudent(db.Model):
    __abstract__ = True

    name: str = db.Column(db.String())
    number: int = db.Column(db.Integer(), unique=True)
    email: str = db.Column(db.String(), unique=True)

    @classmethod
    async def query_by_number(cls, number: int):
        return await cls.query.where(cls.number == number).gino.first()


class StudentModel(BaseStudent):
    __tablename__ = 'student'

    username: str = db.Column(db.String(), primary_key=True)
    password: str = db.Column(db.String())

    @classmethod
    async def query_by_username(cls, username: str):
        return await cls.query.where(cls.username == username).gino.first()


def generate_uuid():
    while True:
        uuid = str(uuid4())[:5]
        if not UnsignedStudentModel.query_by_uuid(uuid):
            return uuid


class UnsignedStudentModel(BaseStudent):
    __tablename__ = 'unsigned_student'

    uuid: str = db.Column(db.String(), default=generate_uuid, unique=True)

    @classmethod
    async def query_by_uuid(cls, uuid: str):
        return await cls.query.where(cls.uuid == uuid).gino.first()
