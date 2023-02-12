import http.client
from .response import Response


class Connection:
    def __init__(self, url):
        self.__connection = http.client.HTTPSConnection(url)

    def send(self, request):
        print('sending request: %s' % request)
        self.__connection.request(request.method, request.url, headers=request.headers, body=request.body)
        response = self.__connection.getresponse()
        data = response.read()
        return Response(response, data)
