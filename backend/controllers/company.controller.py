""" Company Controller - Controlador de Empresa """
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends
from models.conn_db import get_db
from app import app


@app.get("/companies")
def get_companies(db: Session = Depends(get_db)):
    """ Endpoint para obtener todas las empresas"""
    query = text("SELECT * FROM companies")
    result = db.execute(query)
    companies = [dict(row) for row in result]
    return companies
