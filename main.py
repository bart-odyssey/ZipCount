import duckdb

from fastapi import FastAPI, HTTPException
from Adresses.models import (AddressCountResult)
from Adresses.Data.AddressDataLoad import loadAddressData

app = FastAPI()
loadAddressData()


@app.get("/addresses/count/{postalCode}")
def count_addresses(postalCode: str):
    con = duckdb.connect("Adresses/Data/ZipCount.db")
    result = con.execute("SELECT COUNT(*) FROM addresses WHERE PC = ?", (postalCode,)).fetchone()[0]
    r = AddressCountResult(postCode=postalCode, count=result)
    con.close()
    return r

