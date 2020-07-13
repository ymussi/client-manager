import hashlib
import json
import re
from datetime import datetime

import jwt
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

from wishlist.database import session
from wishlist.database.models import User


class Validations:
    
    @classmethod
    def email_validate(cls, email):
        EMAIL_REGEX = re.compile(r"\w{2,50}@\w{2,15}\.[a-z]{2,3}\.?([a-z]{2,3})?")
        if not EMAIL_REGEX.match(email):
            return False
        return True
    
    @classmethod
    def name_is_string(cls, name):
        if name.isdigit():
            return False
        return True
    
    @classmethod
    def value_is_numeral(cls, price):
        if type(price) is float:
            return True
        return False
    
    @classmethod
    def customer_validate(cls, json_data):
        email = json_data.get('email')
        name = json_data.get('email')
        if not email:
            raise BadRequest("Invalid Email.")
        if not name:
            raise BadRequest("Invalid Name.")
        return True
    
    @classmethod
    def product_validate(cls, json_data):
        price = json_data.get('price')
        review_score = json_data.get('reviewScore')
        if not cls.value_is_numeral(price):
            raise BadRequest("Invalid Price type.")
        if not cls.value_is_numeral(review_score):
            raise BadRequest("Invalid reviewScore type.")
        
    @classmethod
    def validate_user_authorization(cls, token, user=None):
        if user is not None:
            query = session.query(User).\
                filter(User.email==user).\
                filter(User.password==token).first()
        else:      
            query = session.query(User).\
                    filter(User.password==token).first()
        
        if not query:
            raise Unauthorized('Your token is not valid or user not exists!')
        return True
    
    @classmethod
    def encode_jwt(cls, user):
        return jwt.encode(user, 'secret', algorithm='HS256')

    @classmethod
    def decode_jwt(cls, jwt):
        return jwt.decode(jwt, 'secret', algorithms=['HS256'])
    
    @classmethod
    def encode_hash(cls, passwd):
        h = hashlib.sha256()
        h.update(passwd.encode())
        return h.hexdigest()
    

class CustomExceptions:
    
    @classmethod
    def search_customer(self, instance):
        if instance:
            customer = {
                "id": instance.id,
                "name": instance.name,
                "email": instance.email,
                "created": datetime.strftime(instance.created, "%Y-%m-%d %H:%M:%S"),
                "updated": datetime.strftime(instance.updated, "%Y-%m-%d %H:%M:%S")
                }
            return customer
        else:
            raise NotFound("Customer not found or not registered.")
    
    @classmethod
    def search_product(self, instance):
        if instance:
            product = {
                "id": instance.id,
                "brand": instance.brand,
                "title": instance.title,
                "image": instance.image,
                "price": float(instance.price),
                "reviewScore": float(instance.reviewScore),
                "created": datetime.strftime(instance.created, "%Y-%m-%d %H:%M:%S"),
                "updated": datetime.strftime(instance.updated, "%Y-%m-%d %H:%M:%S")
                }
            return product
        else:
            raise NotFound("Product not found or not registered.")
        
    @classmethod
    def search_wishlist(self, instance):
        if instance:
            wishlist = {
                "id": instance.id,
                "name": instance.name,
                "email": instance.email,
                "created": datetime.strftime(instance.created, "%Y-%m-%d %H:%M:%S"),
                "updated": datetime.strftime(instance.updated, "%Y-%m-%d %H:%M:%S")
                }
            return customer
        else:
            raise NotFound("Customer not found or not registered.")
