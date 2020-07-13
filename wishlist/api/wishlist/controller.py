from wishlist.api.wishlist.service import WishlistEntity


class WishlistManager:
    @classmethod
    def register_new_wishlist(cls, wishlist):
        return WishlistEntity(wishlist).register()
    
    @classmethod
    def get_wishlist(cls, id):
        return WishlistEntity().get(id)
    
    @classmethod
    def delete_wishlist(cls, client_id, product_id):
        return WishlistEntity().delete(client_id, product_id)
