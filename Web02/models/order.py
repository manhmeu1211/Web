from mongoengine import *
from models.service import Service
from models.user import User

class Order(Document):
    service_id = ReferenceField(Service)
    user_id = ReferenceField(User)
    time_order = DateTimeField()
    is_accepted = BooleanField()