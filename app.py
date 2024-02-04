from fastapi import FastAPI
import uvicorn

from middlewares.middlewares import request_handler
from routers import document_routers

app = FastAPI(title="Document Management service")
app.middleware("http")(request_handler)
app.include_router(document_routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5757)
