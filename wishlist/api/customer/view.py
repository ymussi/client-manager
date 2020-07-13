import logging

from flask import request
from flask_accepts import accepts
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest

from wishlist.api import api
from wishlist.api.customer.controller import CustomerManager
from wishlist.api.customer.schema import CostumerSchema
from wishlist.utils.validations import Validations

log = logging.getLogger(__name__)
ns = api.namespace('customer', description="Manage your consumers.")

parser_internal= ns.parser()

parser = parser_internal.copy()
parser.add_argument('Authorization', type=str, location='headers',
                    help='Authorization Token to get access to Client Manager API', required=True)

@ns.route("/")
@ns.doc(parser=parser)
class Consumer(Resource):
    @accepts(schema=CostumerSchema, api=api)
    def post(self):
        """
        Register a new customer.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        json_data = request.json
        validation = Validations.customer_validate(json_data)
        return CustomerManager.register_new_customer(json_data)
    
    
@ns.route("/<string:email>")
@ns.doc(parser=parser)
class Consumer(Resource):
    @accepts(schema=CostumerSchema, api=api)
    def put(self, email):
        """
        Update a consumer by email.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        json_data = request.json
        data_valid = Validations.customer_validate(json_data)
        return CustomerManager.update_existing_customer(email, json_data)
    
    def get(self, email):
        """
        Search a consumer by email.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        email_valid = Validations.email_validate(email)
        return CustomerManager.get_customer(email)
    
    def delete(self, email):
        """
        Delete a consumer by email.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        email_valid = Validations.email_validate(email)
        return CustomerManager.delete_customer(email)
