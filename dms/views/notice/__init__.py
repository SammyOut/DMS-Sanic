from sanic import Blueprint

notice_blueprint = Blueprint(
    name='notice_blueprint',
    url_prefix='/notice',
)

from views.notice.notice import NoticeListView, NoticeView
notice_blueprint.add_route(NoticeListView.as_view(), '/notice')
notice_blueprint.add_route(NoticeView.as_view(), '/notice/<notice_id:int>')

from views.notice.rule import RuleListView, RuleView
notice_blueprint.add_route(RuleListView.as_view(), '/rule')
notice_blueprint.add_route(RuleView.as_view(), '/rule/<rule_id:int>')
