from fastapi import status as statuscode

from exceptions.base_identified_exception import BaseIdentifiedException
from models.errors.not_found_error import NotFoundError


class NotFoundException(BaseIdentifiedException):
    message = "The entity does not exist"
    code = statuscode.HTTP_404_NOT_FOUND
    model = NotFoundError
