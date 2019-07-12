from sanic.request import Request
from sanic.views import HTTPMethodView


class ExtensionApplyView(HTTPMethodView):
    async def get(self, request: Request, time: int):
        """
        Response Extension Position Which Applied
        """
        pass

    async def post(self, request: Request, time: int):
        """
        Apply Extension
        """
        pass

    async def delete(self, request: Request, time: int):
        """
        Delete Extension
        """
        pass


class ExtensionMapView(HTTPMethodView):
    async def get(self, request: Request, time: int, class_: int):
        """
        Response Extension Map
        """
        pass
