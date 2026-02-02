from models.company import CompanyBase, CompanyCategories

class TreeNode():
    """ Inicializacion Arbol Clase Company """
    def __init__(self, data):
        self.data = data 
        """ 
            Children se pasa como una lista vacia, 
            Y luego en la funcion add_child() se le agrega su hijo a 
            traves del metodo .append()                                             
        """
        self.children = []
        """ El padre queda como un valor vacio """
        self.parent = None
        
    def add_child(self, child) -> object:
        """ Aqui se agrega a la lista children su hijo CompanyCategories """
        self.children.append(child)
        return child
    
    def build_tree(self) -> object:
        """
        Funcion build_tree 
        """
        root = TreeNode(CompanyBase)
        root.add_child(CompanyCategories)
        """ Aqui debo agregar un nodo nuevo para las categorias de productos -> Dos hijos por nodo """
        # root = TreeNode(CompanyCategories)
        # root.add_child(CompanyCategorizedBySize)
        # root.add_child(CompanyCategorizedByBussinessLine)
        # by size 
        # by bussiness line         
        return root
    
    
    
        