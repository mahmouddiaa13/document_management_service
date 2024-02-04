from fastapi import Request

from exceptions.base_api_exception import BaseAPIException


async def request_handler(request: Request, call_next):
    try:
        return await call_next(request)

    except Exception as ex:
        if isinstance(ex, BaseAPIException):
            print(str(ex.response().body))
            return ex.response()

        # Re-raising other exceptions will return internal error 500 to the client
        raise ex
