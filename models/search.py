from pydantic import BaseModel


class req_search(BaseModel):
    store: str
    search: str