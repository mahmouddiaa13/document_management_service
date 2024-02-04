from fastapi import status as statuscode
from models.errors.base_error import BaseError
from fastapi.responses import JSONResponse


class BaseAPIException(Exception):
    message = "Generic error"
    code = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model = BaseError

    def __init__(self, **kwargs):
        kwargs.setdefault("message", self.message)
        self.message = kwargs["message"]
        self.data = self.model(**kwargs)

    def __str__(self):
        return self.message

    def response(self):
        return JSONResponse(
            content=self.data.dict(),
            status_code=self.code
        )

    @classmethod
    def response_model(cls):
        return {cls.code: {"model": cls.model}}
