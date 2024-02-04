# Document Management Service

This document management service allows you to store, retrieve, and search natural language documents. It provides HTTP endpoints for managing documents and supports free-text search queries similar to Google search.

## Installation

### Prerequisites

- Docker

### Steps

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/mahmouddiaa13/document_management_service.git
   cd document_management_service

2. Run Docker Compose to start Elasticsearch, Kibana and fastapi_app containers:

    ```bash
    docker compose -f docker-compose.yml up --build

3. Run Docker Compose to start Elasticsearch and Kibana containers:
## For accessing Swagger UI:
>> navigate to "http://localhost:5757/docs"
## For accessing Kibana:
>> navigate to "http://localhost:5601/app/dev_tools#/console"
## For Testing
1. Change the .env file to set the mode to testing: OPERATION_MODE=testing
2. Down the containers and rebuild.
3. Access the Docker Container    
   ```bash
    docker exec -it fastapi_app /bin/bash
4. Run Pytest  
   ```bash
    pytest
