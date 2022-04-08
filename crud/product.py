
from scraper.amazon_scraper import Amazon
from scraper.flipkart_scraper import Flipkart
from models.product import Product
from database.mongodb import AsyncIOMotorClient


def get_pid(store, url):
    if store == "amazon":
        amz = Amazon()
        return amz.get_productASIN(url)
    elif store == "flipkart":
        flp = Flipkart()
        base_url = flp.get_baseURL(url)
        return flp.get_productID(base_url)


def scrape_product(store, url):
    if store == "amazon":
        amz = Amazon()
        return amz.get_product_data(url)
    elif store == "flipkart":
        flp = Flipkart()
        return flp.get_product_data(url)


def doc_to_product(doc):
    product = Product(  store=doc["store"],
                        product_id=doc["product_id"],
                        base_url=doc["base_url"],
                        product_name=doc["product_name"],
                        product_price=doc["product_price"])
    return product.dict()


def doc_to_product_ondict(doc):
    product = Product(  store=doc["store"],
                        product_id=doc["product_id"],
                        base_url=doc["base_url"],
                        product_name=doc["product_name"],
                        product_price=doc["product_price"])
    return product


async def put_product(product: Product, db: AsyncIOMotorClient):
    result = await db["ecom_product"][product.store].insert_one(product.dict())
    return result


async def get_products(store, db):
    product_list = []
    cursor = db["ecom_product"][store].find({})
    async for doc in cursor:
        product_list.append(doc_to_product(doc))
    return product_list


async def get_product(store, pid, db):
    cursor = await db["ecom_product"][store].find_one({"product_id": pid})
    if cursor:
        return doc_to_product(cursor)


async def get_product_nodict(store, pid, db):
    cursor = await db["ecom_product"][store].find_one({"product_id": pid})
    if cursor:
        return doc_to_product_ondict(cursor)