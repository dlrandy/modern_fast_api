
thing1: str
# thing0
thing1 = 23

def get_thing()->str:
    return "yeah" 

tuple_thing = ("AA","BB","CC")
print("Name is ", tuple_thing[0])

list_thing = ["AA","VV","SSS"]
Name = 0
print("Name is",list_thing[Name])

dict_thing = {
    "name": "yes",
    "num":23
}
print("Name is ", dict_thing["name"])


from collections import namedtuple
CreatureNameTuple = namedtuple("CreatureNamedTuple","name, country, area, desc, aka")

namedtuple_thing = CreatureNameTuple("yy","CN","sss","bula","asdss")

print("named is",namedtuple_thing[0])
print("named is",namedtuple_thing.name)


class CreatureClass():
    def __init__(self, name:str,country:str,area:str,desc:str,aka:str) -> None:
        self.name = name
        self.country = country
        self.area = area
        self.desc = desc
        self.aka = aka
class_thing = CreatureClass("S","s","FF","f","kll")
print("Name is ", class_thing.name)

from dataclasses import dataclass
@dataclass
class CreatureDataClass():
    name:str
    country:str
    area:str
    desc:str
    aka:str

dataclass_thing = CreatureDataClass(
    "sss",
    "ff",
    "xxx",
    "dd",
    "aas"
)

print("Name is ", dataclass_thing.name)