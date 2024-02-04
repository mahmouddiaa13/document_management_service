from fastapi import status as statuscode
from exceptions.base_api_exception import BaseAPIException
from models.errors.base_identified_error import BaseIdentifiedError


class BaseIdentifiedException(BaseAPIException):
    message = "Entity error"
    code = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model = BaseIdentifiedError

    def __init__(self, identifier, **kwargs):
        super().__init__(identifier=identifier, **kwargs)
