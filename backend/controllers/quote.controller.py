""" QUOTE CONTROLLER """
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends
from models.conn_db import get_db
from app import app


@app.get("/quotes")
def get_quotes(db: Session = Depends(get_db)):
    """ Enpooint para obtener todas las cotizaciones """
    query = text("SELECT * FROM QUOTES ORDER BY created_at DESC")
    result = db.execute(query)
    quotes = [dict(row) for row in result]
    return quotes
