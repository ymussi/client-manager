import pytz
from sqlalchemy import (NUMERIC, TIMESTAMP, Column, ForeignKey, Integer,
                        String, func, text)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash

from wishlist.database import Base, Model


class User(Model):
    __tablename__ = 'user'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    username = Column(String(244), nullable=False)
    email = Column(String(244), nullable=False)
    password = Column(String(244), nullable=False)
    

class Customers(Model):
    __tablename__ = 'customer'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(244), nullable=False)
    email = Column(String(244), nullable=False, unique=True)
    wishlist = relationship('Wishlists')
    created = Column(TIMESTAMP, server_default=func.now())
    updated = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    
class Products(Model):
    __tablename__ = 'product'
    id = Column(Integer,unique=True, primary_key=True, autoincrement=True)
    labs_id = Column(String(244), nullable=True, unique=True)
    brand = Column(String(244), nullable=False)
    title = Column(String(244), nullable=False)
    image = Column(String(2048), nullable=False)
    price = Column(NUMERIC, nullable=False)
    wishlist = relationship('Wishlists')
    reviewScore = Column(String(244), nullable=True)
    created = Column(TIMESTAMP, server_default=func.now())
    updated = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    
                   
class Wishlists(Model):
    __tablename__ = 'wishlist'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('customer.id', ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey('product.id', ondelete='CASCADE'))
    customer = relationship('Customers',
                            back_populates='wishlist',
                            primaryjoin="Customers.id == Wishlists.client_id")
    product = relationship('Products',
                            back_populates='wishlist',
                            primaryjoin="Products.id == Wishlists.product_id")
