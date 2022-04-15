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

from crud.search import scrape_search

router = APIRouter()

@router.get("/{store}/{search_str}")
async def getSearch(store: str, search_str: str):
    result = scrape_search(store, search_str)
    if result:
        return result
    else:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"no result found",
        )
