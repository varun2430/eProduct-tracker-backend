from fastapi import APIRouter
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from models.search import req_search
from crud.search import scrape_search

router = APIRouter()

@router.get("/")
async def getSearch(req_search: req_search):
    result = scrape_search(req_search.store, req_search.search)
    if result:
        return result
    else:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"no result found",
        )
