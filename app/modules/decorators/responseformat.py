import functools

from app.modules.exceptions import BaseException
from app.utils.responsebuilder import ResponseBuilder


class FormatResponse:
    def __init__(self, function):
        self.function = function
        self.__name__ = 'FormatResponse'
        functools.update_wrapper(self, self.function)

    def __call__(self, *args, **kwargs):
        try:
            return ResponseBuilder.success_response(self.function(*args, **kwargs))
        except BaseException as e:
            return ResponseBuilder.error_response(msg=str(e), errorcode=e.get_error_code())
        except Exception as e:
            return ResponseBuilder.error_response(msg=e.args, errorcode=500)

# def format_response(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return ResponseBuilder.success_response(func(*args, **kwargs))
#         except BaseException as e:
#             return ResponseBuilder.error_response(msg=str(e), errorcode=e.get_error_code())
#
#     return wrapper
