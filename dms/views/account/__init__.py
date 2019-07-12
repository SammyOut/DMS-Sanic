from sanic import Blueprint

account_blueprint = Blueprint(
    name='account_blueprint',
    url_prefix='/account',
)

from views.account.auth import AuthView
from views.account.signup import SignupView
account_blueprint.add_route(AuthView.as_view(), '/auth')
account_blueprint.add_route(SignupView.as_view(), '/signup')
