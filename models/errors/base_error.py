from pydantic import BaseModel, Field


class BaseError(BaseModel):
    message: str = Field(..., description="Error message or description")
