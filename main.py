from fastapi import FastAPI
from Addresses.Service.AddressService import router
from Addresses.Repository.AddressDataLoad import loadAddressData

loadAddressData()
app = FastAPI()
app.include_router(router)