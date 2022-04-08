from pydantic import BaseModel


class req_product(BaseModel):
    store: str
    url: str

class Price(BaseModel):
    p: str
    dt: str

class Product(BaseModel):
    store: str
    product_id: str
    base_url: str
    product_name: str
    product_price: list[Price] = []