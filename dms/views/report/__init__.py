from sanic import Blueprint


report_blueprint = Blueprint(
    name='report_blueprint',
    url_prefix='/report',
)

from views.report.bug_report import BugReportView
report_blueprint.add_route(BugReportView.as_view(), '/bug')

from views.report.facility_report import FacilityReportView
report_blueprint.add_route(FacilityReportView.as_view(), '/facility')
