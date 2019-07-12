from sanic import response
from sanic.blueprints import Blueprint
from sanic.request import Request

from views.account import account_blueprint
from views.apply import apply_blueprint


blueprint_group = Blueprint.group(
    account_blueprint,
    apply_blueprint,
)


async def ping(request: Request):
    return response.text('pong!')
