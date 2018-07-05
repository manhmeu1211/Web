from mongoengine import *

class Video(Document):
    title = StringField()
    thumbnail = StringField()
    link = StringField()
    views = IntField()
    youtube_id = StringField()
    uploader = StringField()