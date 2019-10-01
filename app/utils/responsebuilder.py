class ResponseBuilder:

    @staticmethod
    def success_response(data=None):
        return {
                   'success': True,
                   'data': data
               }, 200

    @staticmethod
    def error_response(msg=None, errorcode=400):
        return {
                   'success': False,
                   'error_code': errorcode,
                   'error_message': msg or 'Internal Server Error'
               }, errorcode
