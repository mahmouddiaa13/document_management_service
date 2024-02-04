from pydantic import Field

_string = dict(min_length=1)
"""Common attributes for all String fields"""


class DocumentFields:
    document_id = Field(
        description="Document Id",
        example="dsLrao0BS8YJu8TXIXgU",
        **_string
    )
    title = Field(
        description="Document Name",
        example="Document Title",
        **_string
    )
    content = Field(
        description="Document content",
        example="This is the content of the document",
        **_string
    )
    search_text = Field(
        description="search by this text in the documents",
        example="This is the content of the document",
        **_string
    )
    message = Field(
        description="Status message for the response",
        example="Document Created Successfully",
        **_string
    )

