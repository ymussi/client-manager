from wishlist.database import session, Base
from wishlist.database.models import Customers
from wishlist.api.customer.controller import CustomerManager
from wishlist.utils.validations import Validations

from test.runner import clear_db
import unittest

class TestCustomers(unittest.TestCase):
    valid_customer = {"name": "Lu", "email": "lu@luizalabs.com"}
    new_valid_customer = {"name": "Lu2", "email": "lu2@luizalabs.com"}
    invalid_customer = {"name": "123", "email": "lú@@luizalabs.com"}
    
    
    def setUp(self):
        pass
        
    def tearDown(self):
        clear_db(session, Base)
        
    def test_if_name_is_string(self):
        name = self.valid_customer.get('name')
        Validations.name_is_string(name)
    
    def test_if_name_is_not_string(self):
        name = self.invalid_customer.get('name')
        validation = Validations.name_is_string(name)
        self.assertFalse(validation)
        
    def test_if_email_is_valid(self):
        email = self.valid_customer.get('email')
        Validations.email_validate(email)
        
    def test_if_email_is_invalid(self):
        email = self.invalid_customer.get('email')
        validation = Validations.email_validate(email)
        self.assertFalse(validation)
        
    def test_if_method_will_register_a_customer(self):
        CustomerManager.register_new_customer(self.valid_customer)
        
    def test_if_method_will_update_a_customer(self):
        CustomerManager.register_new_customer(self.valid_customer)
        email = self.valid_customer.get('email')
        data = self.new_valid_customer
        CustomerManager.update_existing_customer(email, data)
    
    def test_if_method_get_a_customer(self):
        CustomerManager.register_new_customer(self.valid_customer)
        email = self.valid_customer.get('email')
        CustomerManager.get_customer(email)
        
    def test_if_method_delete_a_customer(self):
        CustomerManager.register_new_customer(self.valid_customer)
        email = self.valid_customer.get('email')
        CustomerManager.delete_customer(email)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
