from typing import List
from pydantic import BaseModel
from models.fields import DocumentFields

__all__ = "Document"


class Document(BaseModel):
    document_id: str = DocumentFields.document_id
    title: str = DocumentFields.title
    content: str = DocumentFields.content


class DocumentCreateResponse(BaseModel):
    message: str = DocumentFields.message
    document_id: str = DocumentFields.document_id


class DocumentCreate(BaseModel):
    title: str = DocumentFields.title
    content: str = DocumentFields.content


class DocumentReadWithPagination(BaseModel):
    documents: List[Document] = []
    page_size: int
    page_number: int
    total: int
