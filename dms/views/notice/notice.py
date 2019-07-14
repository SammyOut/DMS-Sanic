from sanic.request import Request
from sanic.views import HTTPMethodView


class NoticeListView(HTTPMethodView):
    def get(self, request: Request):
        """
        Response Notice List
        """
        pass


class NoticeView(HTTPMethodView):
    def get(self, request: Request, notice_id: int):
        """
        Response Notice
        """
        pass
