#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():

    def __init__(self, *args, **kwargs):

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)

        else:
            storage.new(self)

    def __str__(self):
        
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

        selfDict = self.__dict__.copy()
        selfDict["__class__"] = self.__class__.__name__
        selfDict['created_at'] = self.created_at.isoformat()
        selfDict['updated_at'] = self.updated_at.isoformat()
        return selfDict