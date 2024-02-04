from infrastructure.DB import check_es_connection, get_es_connection_url
from fastapi.testclient import TestClient
from elasticsearch import Elasticsearch
from app import app
import pytest

from setting import get_db_settings, DBSettings

db_settings: DBSettings = get_db_settings()


@pytest.fixture
def test_client():
    elastic_host = get_es_connection_url(db_settings.HOST, db_settings.PORT)
    es = Elasticsearch(
        elastic_host,
        http_auth=(db_settings.USERNAME, db_settings.PWD),
        timeout=20
    )
    check_es_connection(es)

    yield TestClient(app)

    es.indices.delete(index="test_documents", ignore=[400, 404])

