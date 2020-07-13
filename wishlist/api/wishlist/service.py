from wishlist.database.models import Wishlists


class Wishlist:
    
    def __init__(self, wishlist=None):
        self.wishlist = wishlist
    
class WishlistEntity(Wishlist):
    
    def register(self):
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
                "product": row[1],
                "price": float(row[2])
            })
        wishlist['wishlist'] = products
                 
        return wishlist
    
    def delete(self, client_id, product_id):
        Wishlists.delete(client_id=client_id, product_id=product_id)
        wishlist = self.get(client_id)
        return {"status": f"product_id {product_id} removed", "wishlist": wishlist}
