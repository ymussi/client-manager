from wishlist.database import session, Base
from wishlist.database.models import Products
from wishlist.api.product.controller import ProductManager
from wishlist.utils.validations import Validations

from test.runner import clear_db
import unittest

class TestProduct(unittest.TestCase):
    product = {
        "id": 1,
        "price": 100.0,
        "image": "s3/product/test.jpg",
        "brand": "UnitTest Python",
        "title": "Unittest",
        "reviewScore": 10.0
        }
    
    product_updated = {
        "price": 110.0,
        "reviewScore": 9.0
        }
        
    def setUp(self):
        pass
        
    def tearDown(self):
        clear_db(session, Base)
    
    def test_if_price_is_numeric(self):
        price = self.product.get('price')
        Validations.value_is_numeral(price)
    
    def test_if_review_score_is_numeric(self):
        reviewScore = self.product.get('reviewScore')
        Validations.value_is_numeral(reviewScore)
        
    def test_if_method_register_product(self):
        ProductManager.register_new_product(self.product)
    
    def test_if_method_update_a_product(self):
        ProductManager.register_new_product(self.product)
        ProductManager.update_existing_product(1, self.product_updated)
    
    def test_if_method_get_a_product(self):
        ProductManager.register_new_product(self.product)
        ProductManager.get_product(1)
    
    def test_if_method_delete_a_product(self):
        ProductManager.register_new_product(self.product)
        ProductManager.delete_product(1)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
