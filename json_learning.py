import json

p = {"name":"Rithik", "age":19, "city":"Salem", "haschildrn":False, "titles": ["engineer","Datascientist"]}


json1 = json.dumps(p, indent=4, sort_keys=True) #object to json format using dumps for string
json1 = json.dumps(p, indent=4, separators= (':', "="))
print(json1)
with open("p.json","w") as file:
    json.dump(p, file, indent=4)


#decoding or deserialization
#load method
with open('p.json','r')as file:
    p = json.loads(json1)
print(p)




import json

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user = User('max',27)

def encode_user(o):
    if isinstance(o,User):
        return{'name': o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError('object of type is not in json serializable')


# json Encoder method
from json import JSONEncoder
class UserEncoder(JSONEncoder):
   
    def default(self, o):
        if isinstance(o,User):
            return{'name': o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)
# userjson = json.dumps(user, cls=UserEncoder)
userjson = UserEncoder().encode(user)
print(userjson)

#decoder method

def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'],age=dict['age'])
    return dict
#we can access instance variable
user = json.loads(userjson,object_hook=decode_user)
print(type(user))
print(user.name,user.age)
