import mongoengine

# mongo ds149059.mlab.com:49059/c4e18-cms-app -u <dbuser> -p <dbpassword>

host = "ds149059.mlab.com"
port = 49059
db_name = "c4e18-cms-app"
user_name = "manh"
password = "manh1211"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())