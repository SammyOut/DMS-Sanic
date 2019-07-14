from sanic.request import Request
from sanic.views import HTTPMethodView


class FacilityReportView(HTTPMethodView):
    def post(self, request: Request):
        """
        Report Broken Facility
        """
        pass
