from pydantic import BaseModel


class AddressCountResult(BaseModel):
    post_code: str
    count: int
