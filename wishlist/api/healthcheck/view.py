import logging

from flask import request
from flask_restplus import Resource

from wishlist.api import api
from wishlist.api.healthcheck import get_first_record
from wishlist.utils.validations import Validations

log = logging.getLogger(__name__)
ns = api.namespace('healthcheck', description='Communication test.')

parser_internal= ns.parser()

parser = parser_internal.copy()
parser.add_argument('Authorization', type=str, location='headers',
                    help='Authorization Token to get access to Client Manager API', required=True)

@ns.route('/')
@ns.doc(parser=parser)
class HealhCheck(Resource):
    @ns.response(code=400, description='Bad Request')
    def get(self):
        """
        Healhcheck endpoint.
        """
        token = request.headers.get('Authorization')
        auth = Validations.validate_user_authorization(token)
        return get_first_record()
