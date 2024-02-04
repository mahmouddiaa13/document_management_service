from fastapi import status as statuscode
from exceptions.base_identified_exception import BaseIdentifiedException
from models.errors.already_exists_error import AlreadyExistsError


class AlreadyExistsException(BaseIdentifiedException):
    message = "This Title already exists"
    code = statuscode.HTTP_409_CONFLICT
    model = AlreadyExistsError
