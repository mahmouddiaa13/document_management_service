from infrastructure.repository.document_elastic_search_repository import DocumentElasticSearchRepository
from infrastructure.repository.document_base_repository import DocumentBaseRepository
from exceptions.server_not_found_exception import ServerNotFoundException
from infrastructure.ENUMS import DBTYPES
from elasticsearch import Elasticsearch
from typing import List


from setting import get_db_settings, DBSettings

db_settings: DBSettings = get_db_settings()
document_db: DocumentBaseRepository = None


def get_es_connection_url(host: str, port: int) -> List[str]:
    url = f"http://{host}:{port}"
    return [url]


def check_es_connection(es):
    if es.ping():
        print("Connected to Elasticsearch")
    else:
        print("Could not connect to Elasticsearch")
        raise ServerNotFoundException("Elastic Search")


def init_es_document_db() -> DocumentElasticSearchRepository:
    elastic_host = get_es_connection_url(db_settings.HOST, db_settings.PORT)
    es = Elasticsearch(
        elastic_host,
        http_auth=(db_settings.USERNAME, db_settings.PWD),
        timeout=20
    )
    check_es_connection(es)
    document_repository = DocumentElasticSearchRepository(es)
    return document_repository


def get_es_document_db(db: DocumentBaseRepository) -> DocumentBaseRepository:
    if db is None:
        db = init_es_document_db()
    elif db is not DocumentElasticSearchRepository:
        db = init_es_document_db()
    check_es_connection(db.es)
    return db


def get_db() -> DocumentBaseRepository:
    global document_db
    if db_settings.TYPE.lower() == DBTYPES.ELASTICSEARCH.value.lower():
        document_db = get_es_document_db(document_db)
    return document_db
