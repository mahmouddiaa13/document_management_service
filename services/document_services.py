from elasticsearch import NotFoundError
from exceptions.already_exists_exception import AlreadyExistsException
from exceptions.content_not_found_exception import ContentNotFoundException
from infrastructure.repository.document_base_repository import DocumentBaseRepository
from models.document import DocumentCreate, DocumentCreateResponse, Document, DocumentReadWithPagination


class DocumentService:
    def __init__(self, repo: DocumentBaseRepository):
        self.repo = repo

    async def create_document(self, document: DocumentCreate) -> DocumentCreateResponse:
        body = {
            "query": {
                "term": {
                    "title.exact": document.title
                }
            }
        }
        entity_list, _ = await self.repo.search_document(body)
        if entity_list:
            raise AlreadyExistsException(document.title)
        document_id = await self.repo.create(document)
        return DocumentCreateResponse(
            document_id=document_id,
            message=f"Document Created Successfully"
        )

    async def get_document(self, document_id: str) -> Document:
        try:
            entity_list = await self.repo.get(document_id)
        except NotFoundError:
            raise ContentNotFoundException(f"No Document Found with this ID: {document_id}")
        return entity_list

    async def search_document(self, search_text: str, page_number: int = 1,
                              page_size: int = 10) -> DocumentReadWithPagination:
        from_value = (page_number - 1) * page_size
        body = {
            "query": {
                "multi_match": {
                    "query": search_text,
                    "fields": ["title", "content"],
                },
            },
            "from": from_value,
            "size": page_size
        }
        entity_list, total = await self.repo.search_document(body)
        return DocumentReadWithPagination(documents=entity_list, page_number=page_number, page_size=page_size,
                                          total=total)
