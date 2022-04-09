from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database.mongodb_utils import close_mongo_connection, connect_to_mongo
from endpoints.product import router as product_router
from endpoints.search import router as search_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(product_router, prefix="/api/product")
app.include_router(search_router, prefix="/api/search")
