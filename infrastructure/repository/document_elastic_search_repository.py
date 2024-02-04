from infrastructure.repository.document_base_repository import DocumentBaseRepository
from typing import List
from models.document import Document, DocumentCreate
from setting import get_db_settings, DBSettings
from utilities.constants import index_mappings


class DocumentElasticSearchRepository(DocumentBaseRepository):
    """Database adapter for ElasticSearch"""

    def __init__(self, es):
        db_settings: DBSettings = get_db_settings()
        self.index_name = db_settings.INDEX_NAME
        self.es = es
        index_exists = es.indices.exists(index=self.index_name)
        if not index_exists:
            self.es.indices.create(index=self.index_name, body=index_mappings, ignore=400)

    async def create(self, document: DocumentCreate) -> str:
        index_result = self.es.index(index=self.index_name, body=document.__dict__)
        return index_result["_id"]

    async def get(self, document_id: str) -> Document:
        response = self.es.get(index=self.index_name, id=document_id)
        return Document(document_id=document_id, **response["_source"])

    async def search_document(self, body: dict) -> (List[Document], int):
        response = self.es.search(index=self.index_name, body=body)
        hits = response["hits"]["hits"]
        search_results = [Document(document_id=hit["_id"], **hit["_source"]) for hit in hits]
        return search_results, response["hits"]["total"]["value"]
