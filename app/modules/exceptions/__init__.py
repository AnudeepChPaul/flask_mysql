class BaseException(Exception):
    def __init__(self, msg, code):
        self._msg = [ msg ]
        self._code = code or 400

    def add_msg(self, msg):
        self._msg.append(msg)

    def __str__(self):
        return self._msg

    def get_error_code(self):
        return self._code
