from models.products import ProductBase, ProductCategories, ProductFoodCategory, ProductToolCategory

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
        product_categories = TreeNode(ProductCategories)
        product_categories.add_child(ProductFoodCategory)
        product_categories.add_child(ProductToolCategory)
        
        return base_root, product_categories