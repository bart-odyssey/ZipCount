from fastapi import FastAPI
from app.Addresses.Service.AddressService import router
from app.Addresses.Repository.AddressDataLoad import load_address_data

load_address_data()
app = FastAPI()
app.include_router(router)