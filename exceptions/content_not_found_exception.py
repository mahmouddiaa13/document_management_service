from exceptions.not_found_exception import NotFoundException


class ContentNotFoundException(NotFoundException):
    message = "The content does not exist"
