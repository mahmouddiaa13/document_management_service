from models.errors.base_identified_error import BaseIdentifiedError


class NotFoundError(BaseIdentifiedError):
    """The entity does not exist"""
    pass
