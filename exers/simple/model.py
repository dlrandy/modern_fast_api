from pydantic import BaseModel, constr, Field

class Creature(BaseModel):
    name:constr(min_length=2)
    country:str=Field(...,min_length=2)
    area:str
    desc:str
    aka:str

thing2 = Creature(
    name = "sqq",
    country = "qss",
    area="sssss",
    desc="ssssssss",
    aka="ddddddd"
)

print("Name is", thing2.name)