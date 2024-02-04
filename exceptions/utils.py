from typing import Type
from exceptions.base_api_exception import BaseAPIException


def get_exception_responses(*args: Type[BaseAPIException]) -> dict:
    responses = dict()
    for cls in args:
        responses.update(cls.response_model())
    return responses
