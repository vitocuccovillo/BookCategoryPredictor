from functools import partial
from typing import Any, Union

from mongoengine import *
import datetime
from pymongo import MongoClient # different approach
#mongoengine ORM used, (it is not a ORM, but a Document-Object Mapper. In mongo you don't have relations but documents
from mongoengine import QuerySetManager


class Book(Document):
    _id = StringField(required=True)
    bid = IntField()
    title = StringField(max_length=250)
    pageCount = IntField()
    publishedDate = DateTimeField(default=datetime.datetime.now)
    longDescription = StringField()
    status = StringField()
    authors = ListField()
    categories = ListField()
    shortDescription = StringField()
    thumbnailUrl = StringField()
    isbn = StringField()
    meta = {'collection': 'books'}


def getBooks():

    connect('local')
    result = Book.objects
    return result

def GetAllBooks():

    client = MongoClient('localhost', 27017)
    db = client['local']
    result = list(db['books'].find({}))
    client.close()
    return result
