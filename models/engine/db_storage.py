#!/usr/bin/python3
"""
This module defines a class to manage database storage for hbnb clone
"""


import os
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool


class DBStorage():
    """This class manages database storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for the DBStorage class"""
        # Setup environment variables
        os.environ["HBNB_ENV"] = "dev"
        os.environ["HBNB_MYSQL_USER"] = "hbnb_dev"
        os.environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
        os.environ["HBNB_MYSQL_HOST"] = "localhost"
        os.environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"
        os.environ["HBNB_TYPE_STORAGE"] = "db"

        # Retrieve environment variables
        mysql_user = os.environ["HBNB_MYSQL_USER"]
        mysql_pwd = os.environ["HBNB_MYSQL_PWD"]
        mysql_host = os.environ["HBNB_MYSQL_HOST"]
        mysql_database = os.environ["HBNB_MYSQL_DB"]

        # Create engine
        DBStorage.__engine = create_engine(
            f"mysql+mysqldb://\
                {mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_database}",
            pool_pre_ping=True,
            poolclass=NullPool if os.environ["HBNB_ENV"] == "test" else None
            )