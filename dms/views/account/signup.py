from sanic.request import Request
from sanic.views import HTTPMethodView


class SignupView(HTTPMethodView):
    async def get(self, request: Request):
        """
        Check Is UUID valid
        """
        pass

    async def post(self, request: Request):
        """
        Signup
        """
        pass

