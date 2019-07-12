from sanic import Sanic
from views import blueprint_group


def create_app() -> Sanic:
    app_ = Sanic()

    from views import ping
    app_.add_route(ping, '/ping', methods=['GET'])
    app_.blueprint(blueprint_group)

    return app_
