from models.products import ProductBase, ProductCategories, ProductFoodCategory, ProductToolCategory, ProductStatus

class TreeNode():
    def __init__(self, data) -> None: 
        self.data = data
        self.parent = None
        self.children = []
    
    def add_child(self, child) -> object: 
        self.children.append(child)
        return child
    
    def build_tree(self) -> object: 
        base_root = TreeNode(ProductBase)
        base_root.add_child(ProductCategories)
        return base_root