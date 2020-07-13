from wishlist.database import session, Base
from wishlist.database.models import Products
from wishlist.api.wishlist.controller import WishlistManager
from wishlist.api.product.controller import ProductManager
from wishlist.api.customer.controller import CustomerManager
from wishlist.utils.validations import Validations

from test.runner import clear_db
import unittest

class TestWishlist(unittest.TestCase):
    customer = {"id": 1, "name": "Lu", "email": "lu@luizalabs.com"}
    p1 = {
        "id": 1,
        "price": 100.0,
        "image": "s3/product/test.jpg",
        "brand": "UnitTest Python",
        "title": "Unittest",
        "reviewScore": 10.0
        }
    p2 = {
        "id": 2,
        "price": 110.0,
        "image": "s3/product/test.jpg",
        "brand": "UnitTest Python 2",
        "title": "Unittest 2",
        "reviewScore": 20.0
        }
    
    wishlist = {
        "client_id": 1,
        "product_id": 1
        }
    
    wishlist2 = {
        "client_id": 1,
        "product_id": 2
        }
        
    def setUp(self):
        pass
        
    def tearDown(self):
        clear_db(session, Base)
        
    def test_if_method_register_wishlist(self):
        CustomerManager.register_new_customer(self.customer)
        ProductManager.register_new_product(self.p1)
        ProductManager.register_new_product(self.p2)
        WishlistManager.register_new_wishlist(self.wishlist)
        WishlistManager.register_new_wishlist(self.wishlist2)
        duplicate = WishlistManager.register_new_wishlist(self.wishlist)
        self.assertFalse(duplicate.get('status'))
        
    def test_if_method_get_wishlist(self):
        client_id = 1
        WishlistManager.get_wishlist(client_id)

        
if __name__ == "__main__":
    unittest.main(verbosity=2)
