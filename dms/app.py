from sanic import Sanic


def route(app_: Sanic):
    from views import ping
    app_.add_route(ping, '/ping', methods=['GET'])


def create_app() -> Sanic:
    app_ = Sanic()
    route(app_)

    return app_
