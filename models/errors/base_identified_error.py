from pydantic import Field

from models.errors.base_error import BaseError


class BaseIdentifiedError(BaseError):
    identifier: str = Field(..., description="Unique identifier which this error references to")
