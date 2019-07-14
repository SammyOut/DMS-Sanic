from sanic.request import Request
from sanic.views import HTTPMethodView


class RuleListView(HTTPMethodView):
    def get(self, request: Request):
        """
        Response Rule List
        """
        pass


class RuleView(HTTPMethodView):
    def get(self, request: Request, rule_id: int):
        """
        Response Rule
        """
        pass
