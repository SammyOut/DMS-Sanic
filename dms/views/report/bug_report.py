from sanic.request import Request
from sanic.views import HTTPMethodView


class BugReportView(HTTPMethodView):
    def post(self, request: Request):
        """
        Report Bug
        """
        pass
