from wishlist.database import session
from wishlist.database.models import Products
from wishlist.utils.validations import CustomExceptions


class Product:
    
    def __init__(self, product=None):
        self.product = product
    
class ProductEntity(Product):
    
    def register(self):
        product = Products(**self.product)
        resp = product.save()
        self.product['id'] = product.id
        if resp.get('status'):
            return {"status": "Product registered", "product": self.product}
        return resp
    
    def update(self, id):
        resp = Products.update(self.product, id=id)
        if resp.get('status'):
            product = self.get(id)
            return {"status": "Product updated", "product": product}
        return resp.get('msg')
    
    def get(self, id):
        instance = Products.get(id=id)
        product = CustomExceptions.search_product(instance)
        return product
    
    def delete(self, id):
        product = self.get(id)
        if product:
            Products.delete(id=id)
        return {"status": "Product removed", "product": product}
