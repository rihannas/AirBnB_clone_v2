#!/usr/bin/python3

"""DBStorage module"""
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, scoped_session


load_dotenv()


HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_ENV = os.getenv('HBNB_ENV')


# classes = {
#         'BaseModel': BaseModel, 'User': User, 'Place': Place,
#         'State': State, 'City': City, 'Amenity': Amenity,
#         'Review': Review
#     }

classes = [
        'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

class DBStorage():
    """class for db engine"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@localhost/{HBNB_MYSQL_DB}', pool_pre_ping=True, echo=True)

        

    def all(self, cls=None):
        """returns all objects for bd"""
        dic = {}
        if cls is None:
            for obj in self.__session.query().all():
                key = obj.__class_.__name__ + '.' + obj.id
                dic[key] = obj
                return dic

        if cls in classes:
            for obj in self.__session.query(cls).all():
                key = obj.__class_.__name__ + '.' + obj.id
                dic[key] = obj
                return dic
    
    
    def new(self, obj):
        """adds the object to the current database session """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """commits all changes of the current database session """
        self.__session.commit()
    
    def delete(self, obj=None):
        """deletes from the current database session"""
        self.__session.delete()            

    def reload(self):
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity
        from models.user import User

        """creates all tables in the database and creates the current database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session
