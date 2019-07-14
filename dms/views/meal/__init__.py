from sanic import Blueprint

meal_blueprint = Blueprint(
    name='meal_blueprint',
    url_prefix='/meal',
)

from views.meal.meal import MealView
meal_blueprint.add_route(MealView.as_view(), '/<date>')
