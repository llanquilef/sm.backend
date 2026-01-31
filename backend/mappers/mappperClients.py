class Mapper: 
    def __init__(self, name, mapperClients: dict) -> None: 
        self.mapperClients = mapperClients 
     
    DEFAULT_MAPPER = {
        id: 'id',
    }