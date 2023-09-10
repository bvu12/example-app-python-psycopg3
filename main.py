from typing import Union
import uuid

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv

import psycopg
from psycopg.rows import namedtuple_row

load_dotenv()

app = FastAPI()

db_url = os.getenv('COCKROACH_CONNECTION_STRING')
conn = psycopg.connect(db_url,
                       application_name="$ docs_simplecrud_psycopg3",
                       row_factory=namedtuple_row)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/accounts")
def get_accounts():
    accounts = []
    with conn.cursor() as cur:
        rows = cur.execute("SELECT * FROM accounts")
        for row in rows:
            db_account_obj = dict(account_id=row.id, balance=row.balance, country=row.country)
            accounts.append(db_account_obj)

    return {"accounts": accounts}


@app.put("/accounts")
def create_account(balance: int):
    if balance < 0:
        raise Exception("Can't create an account with a negative balance!")

    id = uuid.uuid4()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT into accounts (id, balance) VALUES (%s, %s)", (id, balance))
            conn.commit()
            cur.close()

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

    return {"id": id, "balance": balance}

def main():
    host = "0.0.0.0"  # Use 0.0.0.0 to allow access from external hosts
    port = 8000  # Choose the port you want to use
    reload = True  # Enable auto-reloading for development

    uvicorn.run("main:app", host=host, port=port, reload=reload)

if __name__ == "__main__":
    main()