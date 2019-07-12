from sanic.request import Request
from sanic.views import HTTPMethodView


class GoingoutApplyView(HTTPMethodView):
    async def get(self, request: Request):
        """
        Response Goingout Apply Status
        """
        pass

    async def post(self, request: Request):
        """
        Apply Goingout
        """
        pass

    async def delete(self, reqeuest: Request):
        """
        Delete Goingout Apply
        """
