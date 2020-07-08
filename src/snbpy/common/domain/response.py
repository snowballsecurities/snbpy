class HttpResponse(object):
    def __init__(self):
        self._result_code = None
        self._message = None
        self._data = None
        self._result_str = None

    def succeed(self):
        return '60000' == self._result_code

    @property
    def result_str(self) -> str:
        return self._result_str

    @result_str.setter
    def result_str(self, value: str):
        self._result_str = value

    @property
    def result_code(self) -> str:
        return self._result_code

    @result_code.setter
    def result_code(self, value: str):
        self._result_code = value

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, value: dict):
        self._data = value
