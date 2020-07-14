import requests

from wishlist.api.product.controller import ProductManager
from wishlist.config import config_labs
from wishlist.database.models import Wishlists


class Wishlist:
    
    def __init__(self, wishlist=None):
        self.wishlist = wishlist
    
class WishlistEntity(Wishlist):
    
    def register(self):
        product_id = self.wishlist.get('product_id')
        if product_id.isdigit():
            self.wishlist['id'] = int(product_id)
            resp = Wishlists(**self.wishlist).save()
            if resp.get('status'):
                return {"status": "Wishlist registered", "wishlist": self.wishlist}
            return resp
        else:
            url_labs = config_labs()['url']
            req = requests.get(f"{url_labs}/{product_id}/")
            if req.status_code != 200:
                raise NotFound("Product not found or not registered.")
            product = req.json()
            product['labs_id'] = product.pop('id')
            product_saved = ProductManager.register_new_product(product)
            if not product_saved.get('status'):
                return product_saved.get('msg')
            new_product_id = product_saved.get('product').get('id')
            self.wishlist['product_id'] = new_product_id
            resp = Wishlists(**self.wishlist).save()
            
            if resp.get('status'):
                return {"status": "Wishlist registered", "wishlist": self.wishlist}
            return resp
    
    def get(self, id):
        instance = Wishlists.get_wishlist(client_id=id)
        wishlist = {"client_id": id}
        products = []
        for row in instance:
            products.append({
                "product_id": row[0],
                "product_id_labs": row[1],
                "title": row[2],
                "brand": row[3],
                "price": float(row[4]),
                "image": row[5],
                "review_score": float(row[6]) if row[6] is not None else "null",
            })
        wishlist['wishlist'] = products
                 
        return wishlist
    
    def delete(self, client_id, product_id):
        Wishlists.delete(client_id=client_id, product_id=product_id)
        wishlist = self.get(client_id)
        return {"status": f"product_id {product_id} removed", "wishlist": wishlist}
