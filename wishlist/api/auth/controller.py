from wishlist.api.auth.service import RegistrationEntity


class RegistrationManager:
    @classmethod
    def register_new_user(cls, user):
        return RegistrationEntity(user).register()
    
    @classmethod
    def login_user(cls, user):
        return RegistrationEntity(user).login()
