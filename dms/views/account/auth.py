from sanic.request import Request
from sanic.views import HTTPMethodView


class AuthView(HTTPMethodView):
    async def post(self, request: Request):
        """
        Auth and Generate JWT Token
        """
        pass

    async def patch(self, request: Request):
        """
        Refresh Access Token
        """
        pass
