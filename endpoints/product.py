from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from models.product import req_product
from crud.product import get_pid, get_product, get_product_nodict, get_products, put_product, scrape_product
from database.mongodb import AsyncIOMotorClient, get_database

router = APIRouter()



@router.get("/{store}")
async def getProducts(store:str, db: AsyncIOMotorClient = Depends(get_database)):
    product_list = await get_products(store, db)
    return {"products": product_list}



@router.get("/{store}/{pid}")
async def getProduct(store:str, pid:str, db: AsyncIOMotorClient = Depends(get_database)):
    product = await get_product(store, pid, db)
    if product:
        return {"product": product}
    else:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"{store} product with pid {pid} not found",
        )



@router.post("/")
async def putProduct(req_product: req_product, db: AsyncIOMotorClient = Depends(get_database)):
    pid = get_pid(req_product.store, req_product.url)
    result = await get_product(req_product.store, pid, db)
    if result:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"{req_product.store} product with pid {pid} already exists",
        )
    product = scrape_product(store=req_product.store, url=req_product.url)
    result = await put_product(product, db)
    if result:
        raise HTTPException(
            status_code=HTTP_201_CREATED,
            detail=f"{req_product.store} product with pid {pid} inserted in DB",
        )
    else:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"{req_product.store} product with pid {pid} not found",
        )



@router.put("/{store}/{pid}")
async def updateProduct(store:str, pid:str, db: AsyncIOMotorClient = Depends(get_database)):
    product = await get_product_nodict(store, pid, db)
    if product:
        url = product.base_url
        if store == "flipkart":
            url = url + "&lid"
        elif store == "amazon":
            url = url + "/"

        new_product = scrape_product(product.store, url)

        price_list = product.product_price
        price_list.append(new_product.product_price[0])

        result = await db["ecom_product"][store].replace_one({"product_id": pid}, product.dict())
        if result:
            raise HTTPException(
            status_code=HTTP_200_OK,
            detail=f"{store} product with pid {pid} updated",
        )
    else:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"{store} product with pid {pid} not found",
        )



@router.delete("/{store}/{pid}")
async def deleteProduct(store:str, pid:str, db: AsyncIOMotorClient = Depends(get_database)):
    result = await db["ecom_product"][store].delete_many({"product_id": pid})
    if result:
        return { "detail": f"{store} product with pid {pid} deleted" }
