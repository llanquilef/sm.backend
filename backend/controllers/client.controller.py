""" CLIENTS CONTROLLERS """
from sqlalchemy import text
from fastapi import Depends
from sqlmodel import Session
from app import app
from models.conn_db import get_db


@app.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    """ GET CLIENTS """
    query = text("SELECT * FROM CLIENTS ORDER BY created_at DESC")
    result = db.execute(query)
    clients = [dict(row) for row in result]
    return clients


@app.post("/create-company")
def create_client(db: Session = Depends(get_db)):
    """ CREATE CLIENT BASE  """
    query = text(
        "INSERT INTO client (name, rut, socialReason) VALUES (%(name))")
    result = db.execute(query)
    client = result
    return client
