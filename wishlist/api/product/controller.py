from wishlist.api.product.service import ProductEntity


class ProductManager:
    @classmethod
    def register_new_product(cls, product):
        return ProductEntity(product).register()
    
    @classmethod
    def update_existing_product(cls, id, data):
        return ProductEntity(data).update(id)
    
    @classmethod
    def get_product(cls, id):
        return ProductEntity().get(id)
    
    @classmethod
    def delete_product(cls, id):
        return ProductEntity().delete(id)
