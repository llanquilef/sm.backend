from models.company import CompanyRead, CompanyCreate, CompanyBase
from app import app
from datetime import datetime, timezone

def __init__(self, *args):
    super().init__(*args)
    return self

@app.get
def get_company_info(self, company_id: CompanyBase.id):
    return CompanyRead._get_value(self, company_id)


@app.post
def create_company(self, company: CompanyCreate) -> CompanyBase:
    """
    Create Company with CompanyCreate model based on CompanyBase
    """
    """"
    Here we obtain the id 
    """
    
    self.id = CompanyCreate.id
    self.name = CompanyCreate.name
    self.schema  = CompanyCreate.schema
    self.createdAt = CompanyCreate.createdAt
    
    if self.id == CompanyCreate.id: 
        return IndexError('Ya existe una empresa con el mismo id')
    elif self.name == CompanyCreate.name:
        return 'Ya existe una empresa con el mismo nombre'
    elif self.schema == CompanyCreate.schema: 
        return 'Ya existe una empresa con el mismo esquema'
    elif self.createdAt - datetime.now(timezone.utc): 
        return 'Fecha de creacion invalida'
    
    return company

   
    
    #validatedModelData = company.model_validate(CompanyCreate)
    #data = validatedModelData
    
    # Aqui debo crear metodo de validacion para saber si la data esta llegando como debe 
    # if data:
    #    return 'Modelo de creacion de empresa validado'
    # else:
    #    TypeError('Modelo de datos no validos')
    #return company
 
    