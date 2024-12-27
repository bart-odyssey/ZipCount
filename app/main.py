from fastapi import FastAPI
from app.Addresses.Service.AddressService import router
from app.Addresses.Repository.AddressDataLoad import loadAddressData

loadAddressData()
app = FastAPI()
app.include_router(router)