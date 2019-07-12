from sanic.request import Request
from sanic.views import HTTPMethodView


class StayApplyView(HTTPMethodView):
    async def get(self, request: Request):
        """
        Response Stay Apply Status
        """
        pass

    async def post(self, response: Request):
        """
        Apply Stay
        """
        pass
