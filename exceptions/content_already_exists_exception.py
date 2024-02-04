from exceptions.already_exists_exception import AlreadyExistsException


class ContentAlreadyExistsException(AlreadyExistsException):
    message = "The content already exists"
