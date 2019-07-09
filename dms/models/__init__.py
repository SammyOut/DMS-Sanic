from extension import db

from models.account import StudentModel, UnsignedStudentModel
from models.apply import ExtensionApplyModel, GoingoutApplyModel, MusicApplyModel, StayApplyModel
from models.notice import NoticeModel, RuleModel
from models.point import PointItemModel, PointHistoryModel, PointStatusModel
from models.report import FacilityReportModel


async def init_db():
    await db.set_bind('postgres://postgres@localhost/dms-sanic')
    await db.gino.create_all()
