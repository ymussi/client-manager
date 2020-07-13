from wishlist.api.customer.service import CustomerEntity


class CustomerManager:
    @classmethod
    def register_new_customer(cls, customer):
        return CustomerEntity(**customer).register()
    
    @classmethod
    def update_existing_customer(cls, email, data):
        return CustomerEntity(**data).update(email)
    
    @classmethod
    def get_customer(cls, email):
        return CustomerEntity(email=email).get()
    
    @classmethod
    def delete_customer(cls, email):
        return CustomerEntity(email=email).delete()
