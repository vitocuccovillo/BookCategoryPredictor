from mongoengine import *
import datetime
#mongoengine ORM used, (it is not a ORM, but a Document-Object Mapper. In mongo you don't have relations but documents


class Book(Document):
    _id = StringField(required=True)
    title = StringField(max_length=250)
    pageCount = IntField()
    publishedDate = DateTimeField(default=datetime.datetime.now)
    longDescription = StringField()
    status = StringField()
    authors = GenericEmbeddedDocumentField()
    categories = GenericEmbeddedDocumentField()
    meta = {'collection': 'books'}
    shortDescription = StringField()
    thumbnailUrl = StringField()
    isbn = StringField()


def getBooks():

    connect('local')
    print('Connected with local, collection books')

    for b in Book.objects:
        print(b.title)