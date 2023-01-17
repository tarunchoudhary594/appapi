from flask import Blueprint
from app.v1.users import views as sample_subapp_views


v1 = Blueprint('v1', __name__)


# subapp1 urls
sample_subapp_prefix = '/users'

v1.add_url_rule(sample_subapp_prefix + '/getUserName', view_func=sample_subapp_views.GetUserName.as_view('endpoint_1'))


