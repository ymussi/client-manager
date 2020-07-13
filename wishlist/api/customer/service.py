import json

from werkzeug.exceptions import NotFound

from wishlist.database import session
from wishlist.database.models import Customers
from wishlist.utils.validations import CustomExceptions


class Customer:
    
    def __init__(self, id=None, name=None, email=None):
        self.id = id
        self.name = name
        self.email = email
    
class CustomerEntity(Customer):
    
    def register(self):
        customer = Customers()
        if self.id is not None:
            customer.id = self.id
        customer.name = self.name
        customer.email = self.email
        resp = customer.save()
        if resp.get('status'):
            reg = self.get()
            return {"status": "Customer registered", "customer": reg}
        return resp.get('msg')
    
    def update(self, email):
        data = {"name": self.name, "email": self.email}
        self.email = data.get('email')
        resp = Customers.update(data, email=email)
        if resp.get('status'):
            customer = self.get()
            return {"status": "Customer updated", "customer": customer}
        return resp.get('msg')
    
    def get(self):
        instance = Customers.get(email=self.email)
        customer = CustomExceptions.search_customer(instance)
        return customer
    
    def delete(self):
        customer = self.get()
        if customer:
            Customers.delete(email=self.email)
        return {"status": "Customer removed", "customer": customer}
