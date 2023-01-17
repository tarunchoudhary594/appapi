from flask import request
from functools import wraps
from app.common_utils import render_error_response, extract_params


def validate_request(func):

    def extract_headers():
        return dict(request.headers)

    @wraps(func)
    def decorated_function(*args, **kwargs):
        params = extract_params()
        headers = extract_headers()
        return func(params=params, headers=headers, *args, **kwargs)

    return decorated_function
