import logging

from flask import request
from flask_accepts import accepts
from flask_restplus import Resource

from wishlist.api import api
from wishlist.api.auth.controller import RegistrationManager
from wishlist.api.auth.schema import LoginSchema, RegisterSchema

log = logging.getLogger(__name__)
ns = api.namespace('register', description='Registration and login.')


@ns.route('/')
class Register(Resource):
    @accepts(schema=RegisterSchema, api=api)
    def post(self):
        """
        Register user.
        """
        json_data = request.json
        email = json_data.get('email')
        email_valid = Validations.email_validate(email)
        return RegistrationManager.register_new_user(json_data)
    
@ns.route('/login')
class Login(Resource):
    @accepts(schema=LoginSchema, api=api)
    def post(self):
        """
        Login user.
        """
        json_data = request.json
        email = json_data.get('email')
        email_valid = Validations.email_validate(email)
        return RegistrationManager.login_user(json_data)
