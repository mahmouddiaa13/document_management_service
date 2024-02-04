from .testing_data import doc_test_case_1, doc_test_case_2, doc_test_case_3
from fastapi import status as statuscode
import pytest


# ********************This is an example of how I would test the Service**************************
@pytest.mark.parametrize("body, expected_result", [
    (doc_test_case_1, statuscode.HTTP_201_CREATED),
    (doc_test_case_2, statuscode.HTTP_422_UNPROCESSABLE_ENTITY),
    (doc_test_case_3, statuscode.HTTP_422_UNPROCESSABLE_ENTITY)
])
@pytest.mark.asyncio
async def test_create_document(test_client, body, expected_result):
    response = test_client.post('/document', json=body)
    print(response.json())
    assert response.status_code == expected_result
