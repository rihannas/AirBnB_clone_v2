#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

# from sqlalchemy import create_engine
# from models.base_model import Base
# from dotenv import load_dotenv
# import os
# from sqlalchemy.orm import sessionmaker
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review


# # load the env variables in the .env file
# load_dotenv()


# class DBStorage():
#     """This class manages storage of hbnb models in db"""
#     __engine = None
#     __session = None

#     def __init__(self):
#         '''Create db engine'''
#         DBStorage.__engine = create_engine(
#             "mysql+mysqldb://{}:{}@{}/{}".
#             format(os.getenv('HBNB_MYSQL_USER'),
#                    os.getenv('HBNB_MYSQL_PWD'),
#                    os.getenv('HBNB_MYSQL_HOST'),
#                    os.getenv('HBNB_MYSQL_DB')),
#             pool_pre_ping=True, echo=True)
#         #  pool_pre_ping checks if the connection is still alive and re-connects if not.

#     def all(self, cls=None):
#         """
#         Query on the current database session (self.__session)
#         all objects depending of the class name

#         Returns a dict with key = <class-name>.<object-id>
#         value = object
#         """
#         # creating the session
#         self.__session = sessionmaker()(bind=DBStorage.__engine)
#         dataDict = {}
#         if cls is None:
#             datas = self.__session.query(
#                 User, State, City, Amenity, Place, Review).all()
#             for data in datas:
#                 key = str(data.__class__.__name__) + '.' + str(data.id)
#                 dataDict[key] = data
#             return dataDict

#         else:
#             datas = self.__session.query(cls).all()
#             for data in datas:
#                 key = str(data.__class__.__name__) + '.' + str(data.id)
#                 dataDict[key] = data
#             return dataDict

#     def new(self, obj):
#         '''
#         add the object to the current database session (self.__session
#         '''

# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine, Base
# from sqlalchemy.orm import sessionmaker, scoped_session
# from models.state import State
# from models.city import City
# from models.review import Review
# from models.place import Place
# from models.amenity import Amenity
# from models.user import User


# load_dotenv()


# HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
# HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
# HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
# HBNB_ENV = os.getenv('HBNB_ENV')


# # classes = {
# #         'BaseModel': BaseModel, 'User': User, 'Place': Place,
# #         'State': State, 'City': City, 'Amenity': Amenity,
# #         'Review': Review
# #     }

# classes = [
#         'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

# class DBStorage():
#     """class for db engine"""

#     __engine = None
#     __session = None

#     def __init__(self):
#         self.__engine = create_engine(
#             f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@localhost/{HBNB_MYSQL_DB}', pool_pre_ping=True, echo=True)

        

#     def all(self, cls=None):
#         """returns all objects for bd"""
#         dic = {}
#         if cls is None:
#             for obj in self.__session.query().all():
#                 key = obj.__class_.__name__ + '.' + obj.id
#                 dic[key] = obj
#                 return dic

#         if cls in classes:
#             for obj in self.__session.query(cls).all():
#                 key = obj.__class_.__name__ + '.' + obj.id
#                 dic[key] = obj
#                 return dic
    
    
#     def new(self, obj):
#         """adds the object to the current database session """
#         self.__session.add(obj)
#         self.__session.commit()

#     def save(self):
#         """commits all changes of the current database session """
#         self.__session.commit()
    
#     def delete(self, obj=None):
#         """deletes from the current database session"""
#         self.__session.delete()            

#     def reload(self):
#         """creates all tables in the database and creates the current database session"""
#         from models.base_model import Base
#         from models.user import User
#         from models.place import Place
#         from models.state import State
#         from models.city import City
#         from models.amenity import Amenity
#         from models.review import Review

#         if HBNB_ENV == "test":
#             Base.metadata.drop_all(self.__engine)

#         Base.metadata.create_all(self.__engine)
#         session = sessionmaker(bind=self.__engine, expire_on_commit=False)
#         Session = scoped_session(session)
#         self.__session = Session

#!/usr/bin/python3
"""This script will create a new database"""
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """This class is the beginning of database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """This will initiate the database"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """This function will query on the current database session"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        new_dict = {}
        if cls:
            for value in self.__session.query(cls).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
        else:
            for value in self.__session.query(User).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            for value in self.__session.query(Place).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            for value in self.__session.query(State).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            for value in self.__session.query(City).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
            # for value in self.__session.query(Amenity).all():
                # name = type(value).__name__ + '.' + value.id
                # new_dict[name] = value
            for value in self.__session.query(Review).all():
                name = type(value).__name__ + '.' + value.id
                new_dict[name] = value
        return new_dict

    def new(self, obj):
        """This function will add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """This function will commit all changes of the current database
           session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """This function will delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """This will create all database features"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()

    def close(self):
        """This function will close a session"""
        self.__session.close()
        self.reload()