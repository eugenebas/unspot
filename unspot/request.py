from urllib.parse import urlencode


class Request:
    def __init__(self, url, method, authorization_token, params=None, body=None):
        if params is None:
            self._url = url
        else:
            self._url = url + '?' + urlencode(params)
        self._method = method
        self._headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en',
            'authorization': authorization_token,
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
        if body is not None:
            self._headers['content-length'] = len(body)
            self._headers['content-type'] = 'application/json;charset=UTF-8'
        self._body = body

    @property
    def url(self):
        return self._url

    @property
    def method(self):
        return self._method

    @property
    def headers(self):
        return self._headers

    @property
    def body(self):
        return self._body

    def __str__(self):
        headerStr = ''
        for key, value in self.headers.items():
            headerStr += '\t"%s": "%s"\n' % (key, value)
        headerStr = '{\n%s}' % headerStr
        return '%s %s\n----\n%s\n-----\n%s\n' % (self.url, self.method, headerStr, self._body)