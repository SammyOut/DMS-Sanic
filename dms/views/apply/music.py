from sanic.request import Request
from sanic.views import HTTPMethodView


class MusicApplyView(HTTPMethodView):
    def get(self, request: Request, weekday: int):
        """
        Response Music Apply Status
        """
        pass

    def post(self, request: Request, weekday: int):
        """
        Apply Music
        """
        pass

    def delete(self, request: Request, weekday: int):
        """
        Delete Music apply on the weekday
        """
        pass
