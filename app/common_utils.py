import json
from flask import Response, request


def render_success_response(response, msg='', status=1):
    body = {
        's': status,
        'm': msg,
        'd': response
    }
    return Response(json.dumps(body), status=200, content_type='application/json')


def render_error_response(msg, status):
    body = {
        's': 0,
        'm': msg,
        'd': dict()
    }
    return Response(json.dumps(body), status=status, content_type='application/json')


def extract_params():
    if request.method == 'POST':
        if request.content_type == 'application/x-www-form-urlencoded':
            params = request.form
        elif 'multipart/form-data' in request.content_type:
            params = request
        else:
            params = request.get_json()
        return params
    else:
        params = request.args
        parsed_params = dict()
        for key, val in dict(params).items():
            if isinstance(val, list) and val:
                parsed_params.update({key: val[0]})
            else:
                parsed_params.update({key: val})
        return parsed_params
