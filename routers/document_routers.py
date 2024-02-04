from fastapi import APIRouter, Depends, status as statuscodes
from exceptions.content_already_exists_exception import ContentAlreadyExistsException
from exceptions.content_not_found_exception import ContentNotFoundException
from exceptions.utils import get_exception_responses
from infrastructure.DB import get_db
from infrastructure.repository.document_base_repository import DocumentBaseRepository
from models.document import DocumentCreate, DocumentCreateResponse, Document, DocumentReadWithPagination
from services.document_services import DocumentService

router = APIRouter()


@router.post(
    "/document",
    description="Create a new document record",
    response_model=DocumentCreateResponse,
    status_code=statuscodes.HTTP_201_CREATED,
    responses=get_exception_responses(ContentAlreadyExistsException),
    tags=["document"]
)
async def create_document(
        document: DocumentCreate,
        repository: DocumentBaseRepository = Depends(get_db)):
    service = DocumentService(repository)
    result = await service.create_document(document=document)
    return result


@router.get(
    "/document/search",
    description="Free Text Search",
    response_model=DocumentReadWithPagination,
    tags=["document"]
)
async def search(
        search_text: str,
        page_number: int = 1,
        page_size: int = 10,
        repository: DocumentBaseRepository = Depends(get_db)):
    service = DocumentService(repository)
    result = await service.search_document(search_text, page_number, page_size)
    return result


@router.get(
    "/document/{document_id}",
    description="Get Document by id",
    response_model=Document,
    responses=get_exception_responses(ContentNotFoundException),
    tags=["document"]
)
async def get_document(
        document_id: str,
        repository: DocumentBaseRepository = Depends(get_db)):
    service = DocumentService(repository)
    result = await service.get_document(document_id)
    return result
