from sanic.blueprints import Blueprint

apply_blueprint = Blueprint(
    name='apply_blueprint',
    url_prefix='/apply',
)

from views.apply.extension import ExtensionApplyView, ExtensionMapView
apply_blueprint.add_route(ExtensionApplyView.as_view(), '/extension/<time:int>')
apply_blueprint.add_route(ExtensionMapView.as_view(), '/extension/map/<time:int>/<class_:int>')

from views.apply.goingout import GoingoutApplyView
apply_blueprint.add_route(GoingoutApplyView.as_view(), '/goingout')

from views.apply.music import MusicApplyView
apply_blueprint.add_route(MusicApplyView.as_view(), '/music/<weekday:int>')

from views.apply.stay import StayApplyView
apply_blueprint.add_route(StayApplyView.as_view(), '/stay')
