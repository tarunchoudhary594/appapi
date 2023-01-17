class SubApp1Service:

    def __init__(self, params, headers):
        self.params = params
        self.headers = headers

    def get_static_api_response(self):
        return self.params, 'success'
