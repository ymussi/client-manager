from wishlist.database import session, Base
from wishlist.api.auth.controller import RegistrationManager
from wishlist.utils.validations import Validations

from test.runner import clear_db
import unittest

class TestCustomers(unittest.TestCase):
    valid_user = {"username": "Lu", "email": "lu@luizalabs.com", "password": "magalu2020"}
    
    def setUp(self):
        pass
        
    def tearDown(self):
        clear_db(session, Base)
        
    def test_if_email_is_valid(self):
        email = self.valid_user.get('email')
        Validations.email_validate(email)
        
    def test_if_method_will_register_a_user(self):
        RegistrationManager.register_new_user(self.valid_user)
    
    def test_if_method_get_a_customer(self):
        RegistrationManager.register_new_user(self.valid_user)
        RegistrationManager.login_user(self.valid_user)
        
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
