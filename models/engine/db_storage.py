#!/usr/bin/python3
"""
This module defines a class to manage database storage for hbnb clone
"""


from os import environ
from sqlalchemy.pool import NullPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """This class manages database storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for the DBStorage class"""
        # Setup environment variables
        environ["HBNB_ENV"] = "dev"
        environ["HBNB_MYSQL_USER"] = "hbnb_dev"
        environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
        environ["HBNB_MYSQL_HOST"] = "localhost"
        environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"
        environ["HBNB_TYPE_STORAGE"] = "db"

        # Retrieve environment variables
        mysql_user = environ["HBNB_MYSQL_USER"]
        mysql_pwd = environ["HBNB_MYSQL_PWD"]
        mysql_host = environ["HBNB_MYSQL_HOST"]
        mysql_database = environ["HBNB_MYSQL_DB"]

        # Create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(environ['HBNB_MYSQL_USER'],
                                              environ['HBNB_MYSQL_PWD'],
                                              environ['HBNB_MYSQL_HOST'],
                                              environ['HBNB_MYSQL_DB']),
                                    pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """Query objects from the current database session."""
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            objects = {obj.__class__.__name__ + '.' + obj.id: obj
                       for obj in self.__session.query(cls)}
        else:
            for cls in classes:
                objects.update({obj.__class__.__name__ + '.' + obj.id: obj
                                for obj in self.__session.query(cls)})
        return objects

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables in the database and create a new session."""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
