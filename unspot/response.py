import json


class Response:
    def __init__(self, response, data):
        self._response = response
        self._data = data

    def text(self):
        return self._data.decode()

    def json(self):
        return json.loads(self.text())

    def json_string(self):
        return json.dumps(self.json(), indent=4).encode('latin1').decode('unicode_escape')

    def __bool__(self):
        return self._response.status == 200

    def __str__(self):
        return "%s %s\n-----\n%s\n-----\n%s" % (self._response.status, self._response.reason, self._response.headers, self._data)