from typing import List

from models.document import Document, DocumentCreate


class DocumentBaseRepository:
    async def create(self, create: DocumentCreate) -> str:
        """create single entity in the db"""
        raise NotImplementedError()

    async def get(self, document_id: str) -> Document:
        """get an entity by a document_id"""
        raise NotImplementedError()
    
    async def search_document(self, query: dict) -> (List[Document], int):
        """search for entities by a text"""
        raise NotImplementedError()

