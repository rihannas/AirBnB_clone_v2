#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#  class BaseModel that defines all common attributes/methods for other classes:


class BaseModel():
    """Base class for all models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        # if kwargs is not empty
        if kwargs:
            if '__class__' in kwargs.keys():
                # remove the key __class__ from kwargs
                kwargs.pop('__class__')

            for key, item in kwargs.items():
                if key == 'created_at':
                    cdt = datetime.strptime(item, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, cdt)
                elif key == 'updated_at':
                    udt = datetime.strptime(item, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, udt)
                else:
                    setattr(self, key, item)

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    # magic method which represents a class object as str

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    # public methods

    def save(self):
        # updates updated_at with current datetime.
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        # return dict - which contains all keys/values of __dict__ plus:
        # 1. '__class__' key must be added to dictionary
        # 2. created_at and updated_at in ISO format

        dic = {}

        # what is the difference of using copy() or not.
        dic = self.__dict__.copy()
        # dic['id'] = self.id no need as __dict__ has the id
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        key = "_sa_instance_state"

        if key in dic.keys():
            del dic[key]

        return dic

    def delete(self):
        """
        deletes the current instance from storage
        """
        from models import storage
        storage.delete(self)