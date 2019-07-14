from sanic.request import Request
from sanic.views import HTTPMethodView


class MealView(HTTPMethodView):
    def get(self, request: Request, date: str):
        """
        Response meal on parameter date
        """
        pass
