from time import time
from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # print('BEFORE IN MIDDLEWARE')
        start = time()

        response = self.get_response(request)

        end = time()
        # print(f'AFTER IN MIDDLEWARE {end - start}')

        reqResLog = RequestResponseLog(
            path=request.path,
            request_method=request.method,
            time=end-start
        )
        reqResLog.save()
        return response
