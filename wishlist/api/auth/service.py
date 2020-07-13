import hashlib
import json

from werkzeug.exceptions import NotFound

from wishlist.database import session
from wishlist.database.models import User
from wishlist.utils.validations import Validations


class Registration:
    
    def __init__(self, user):
        self.user = user
    
class RegistrationEntity(Registration):
    
    def register(self):
        token = Validations.encode_hash(self.user.get('password'))
        user = User()
        user.username = self.user.get('username')
        user.email = self.user.get('email')
        user.password = token
        resp = user.save()
        if resp.get('status'):
            return {"status": "user registered", "token": token}
        return resp.get('msg')
    
    def login(self):
        user = self.user.get('email')
        token = Validations.encode_hash(self.user.get('password'))
        user = Validations.validate_user_authorization(token, user=user)
        return {"status": "Successful login!", "token": token}
