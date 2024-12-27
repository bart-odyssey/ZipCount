from fastapi import APIRouter

from app.Addresses.Repository.AddressRepo import count_addresses_by_postal_code
from app.Addresses.Service.models import AddressCountResult

COUNT_API_PATH = "/count"

router = APIRouter(
    prefix="/addresses",
    tags=["addresses"]
)


class AddressService:
    @router.get(COUNT_API_PATH + "/{postal_code}")
    def count_addresses(postal_code: str):
        address_count = count_addresses_by_postal_code(postal_code=postal_code)
        return AddressCountResult(post_code=postal_code, count=address_count)