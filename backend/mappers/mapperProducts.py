from models.products import ProductBase, ProductCreate
from utils.timestamps.DateTimeToUTC import get_time_to_utc

class Mapper:
    """ """
        
    def __init__(self, mapper: dict) -> dict: 
        self.mapper = mapper
    
 
    DEFAULT_MAPPER = {
        # Product Base
        'id': ProductBase.id, 
        'name': ProductBase.name,
        'description': ProductBase.description,
        ''
        
        #'companyId': ProductBase.
        # ProductCreate
        
        }
    
    """
    Diccionario Mapper - Aqui se inicializa ({})
    """
    
    mapperProducts = {}
    