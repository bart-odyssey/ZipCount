from pydantic import BaseModel


class AddressCountResult(BaseModel):
    postCode: str
    count: int
