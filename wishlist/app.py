from flask import Blueprint, Flask
from flask_cors import CORS

from wishlist.api import api
from wishlist.api.auth.view import ns as register
from wishlist.api.customer.view import ns as customer
from wishlist.api.healthcheck.view import ns as healthcheck
from wishlist.api.product.view import ns as product
from wishlist.api.wishlist.view import ns as wishlist
from wishlist.config import config_db


def create_app(config_filename=None):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    connect_string = config_db()['database_uri']
    app.config['SQLALCHEMY_DATABASE_URI'] = connect_string
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False

    blueprint = Blueprint('login', __name__)
    api.init_app(blueprint)
    api.add_namespace(healthcheck, "/healthcheck")
    api.add_namespace(customer, '/customer')
    api.add_namespace(product, '/product')
    api.add_namespace(wishlist, '/wishlist')
    api.add_namespace(register, '/register')

    app.register_blueprint(blueprint)
    app.teardown_appcontext(shutdown_session)
    return app
    
def shutdown_session(exception=None):
    from wishlist.database import session
    session.remove()
