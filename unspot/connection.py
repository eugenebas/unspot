import http.client
from .response import Response


class Connection(http.client.HTTPSConnection):
    def __init__(self, url):
        super().__init__(url)

    def send_request(self, request):
        print('sending request: %s' % request)
        self.request(request.method, request.url, headers=request.headers, body=request.body)
        response = self.getresponse()
        data = response.read()
        return Response(response, data)
