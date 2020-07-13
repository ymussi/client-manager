import logging

from flask import request
from flask_accepts import accepts
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest

from wishlist.api import api
from wishlist.api.product.controller import ProductManager
from wishlist.api.product.schema import ProductSchema
from wishlist.utils.validations import Validations

log = logging.getLogger(__name__)
ns = api.namespace('product', description="Manage your product.")

parser_internal= ns.parser()

parser = parser_internal.copy()
parser.add_argument('Authorization', type=str, location='headers',
                    help='Authorization Token to get access to Client Manager API', required=True)

@ns.route("/")
@ns.doc(parser=parser)
class Product(Resource):
    @accepts(schema=ProductSchema, api=api)
    def post(self):
        """
        Register a new Product.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        json_data = request.json
        validation = Validations.product_validate(json_data)
        return ProductManager.register_new_product(json_data)
    
    
@ns.route("/<string:id>")
@ns.doc(parser=parser)
class Product(Resource):
    @accepts(schema=ProductSchema, api=api)
    def put(self, id):
        """
        Update a Product by id.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        json_data = request.json
        validation = Validations.product_validate(json_data)
        return ProductManager.update_existing_product(id, json_data)
    
    def get(self, id):
        """
        Search a Product by id.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        return ProductManager.get_product(id)
    
    def delete(self, id):
        """
        Delete a Product by id.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        return ProductManager.delete_product(id)
