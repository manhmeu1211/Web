from mongoengine import *

#1 Design database
class Customer(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    phone = StringField()
    email = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()