import mongoengine

# mongodb://manh:manhmeu1211@ds263500.mlab.com:63500/app

host = "ds263500.mlab.com"
port = 63500
db_name = "app"
user_name = "manh"
password = "manhmeu1211"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())