from wishlist.api import api
from wishlist.api.wishlist.controller import WishlistManager
from wishlist.api.wishlist.schema import WishlistSchema
from wishlist.utils.validations import Validations
from werkzeug.exceptions import BadRequest
from flask_restplus import Resource
from flask_accepts import accepts
from flask import request

import logging

log = logging.getLogger(__name__)
ns = api.namespace('wishlist', description="Manage your wishlist.")

parser_internal= ns.parser()

parser = parser_internal.copy()
parser.add_argument('Authorization', type=str, location='headers',
                    help='Authorization Token to get access to Client Manager', required=True)

@ns.route("/")
@ns.doc(parser=parser)
class Wishlist(Resource):
    @accepts(schema=WishlistSchema, api=api)
    def post(self):
        """
        Register new wishlist
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        json_data = request.json
        return WishlistManager.register_new_wishlist(json_data)

@ns.route("/<string:client_id>")
@ns.doc(parser=parser)
class Wishlist(Resource):    
    def get(self, client_id):
        """
        Search wishlist by client_id
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        return WishlistManager.get_wishlist(client_id)
    
@ns.route("/<string:client_id>/<string:product_id>")
@ns.doc(parser=parser)
class Wishlist(Resource):
    def delete(self, client_id, product_id):
        """
        Delete product from wishlist by client_id and product_id
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        
        return WishlistManager.delete_wishlist(client_id, product_id)
