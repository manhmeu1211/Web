from mongoengine import *

class User(Document):
    fullname = StringField(required = True)
    email = StringField(required = True)
    username = StringField()
    password = StringField()