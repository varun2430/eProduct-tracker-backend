from pydantic import BaseModel


class SearchProduct(BaseModel):
    store: str
    product_id: str
    base_url: str
    img_src: str
    product_name: str
    product_description: str
    product_price: str
    dt: str