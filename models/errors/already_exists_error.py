from models.errors.base_identified_error import BaseIdentifiedError


class AlreadyExistsError(BaseIdentifiedError):
    """An entity being created already exists"""
    pass
