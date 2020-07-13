from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import asc, func
from sqlalchemy_utils import generic_repr

from wishlist.conector.mysql import mysql_engine

session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=mysql_engine("client_manager")))

Base = declarative_base()
Base.query = session.query_property()


@generic_repr
class CRUDMixin:
    """
    Mixin that adds convenience methods for CRUD (create, read, update, delete) operations.
    """
    def save(self, commit=True):
        """Save the record."""
        session.add(self)
        if commit:
            try:
                session.commit()
                return {"status": True}
            except SQLAlchemyError as e:
                resp = {"msg": str(e.__dict__['orig']), "status": False}
                print(f'Error in class CustomerEntity, exception: {resp}')
                session.rollback()
                return resp 
            finally:
                session.close()
        return self

    def as_dict(self, filter_columns=None, enum_values=None):
        """
        :param `filter_columns` lista de colunas que serão filtradas do resultado final
        :param `enum_values`  flag para indicar se você deseja retornar os valores em tipo Enum ou seus Valores.
        """
        dret = {}

        if not filter_columns:
            filter_columns = []

        for column in self.__table__.columns:
            if column.name in filter_columns:
                continue

            val = getattr(self, column.name)

            if enum_values:
                if isinstance(val, Enum):
                    val = val.value

            dret[column.name] = val
        return dret
    
    @classmethod
    def get(cls, **kwargs):
        instance = session.query(cls).filter_by(**kwargs).first()   
        return instance
    
    @classmethod
    def get_wishlist(cls, client_id):        
        query = text("""select p.id as product_id, p.title as product_name, p.price as price from client_manager.wishlist as l
                    inner join client_manager.product as p on l.product_id = p.id
                    where l.client_id=:id""").bindparams(id=client_id)
        wishlist = session.execute(query)
        return wishlist
    
    @classmethod
    def delete(cls, commit=True, **kwargs):
        instance = session.query(cls).filter_by(**kwargs).delete()
        if commit:
            try:
                session.commit()
            except Exception as exc:
                print(f'Error in update, exception: {exc} ')
                session.rollback()
                raise
            finally:
                session.close()
        return cls
    
    @classmethod
    def update(cls, data, commit=True, **kwargs):
        """
        :kwargs must be `id` or `email`
        :data must be a dict
        """
        data['updated'] = datetime.today()
        email = kwargs.get('email')
        id = kwargs.get('id')
        if email:
            instance = session.query(cls).filter(cls.email == email).update(data)
        if id:
            instance = session.query(cls).filter(cls.id == id).update(data)

        if commit:
            try:
                if instance == 0:
                    raise SQLAlchemyError('Record not found!') 
                session.commit()
                return {"status": True}
            except Exception as exc:
                resp = {"msg": str(exc), "status": False}
                print(f'Error in update, exception: {exc} ')
                session.rollback()
                return resp
            finally:
                session.close()
        return cls


class Model(CRUDMixin, Base):
    __abstract__ = True

    @classmethod
    def get_by_id(cls, record_id):
        """Get record by ID."""
        if any(
                (isinstance(record_id, (str, bytes)) and record_id.isdigit(),
                 isinstance(record_id, (int, float))),
        ):
            return cls.query.get(int(record_id))
        return None
