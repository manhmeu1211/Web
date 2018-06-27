from mongoengine import *

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()