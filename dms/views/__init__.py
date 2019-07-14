from sanic import response
from sanic.blueprints import Blueprint
from sanic.request import Request

from views.account import account_blueprint
from views.apply import apply_blueprint
from views.meal import meal_blueprint
from views.notice import notice_blueprint
from views.report import report_blueprint

blueprint_group = Blueprint.group(
    account_blueprint,
    apply_blueprint,
    meal_blueprint,
    notice_blueprint,
    report_blueprint,
)


async def ping(request: Request):
    return response.text('pong!')
