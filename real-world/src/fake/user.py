from model.user import User
from errors import Missing,Duplicate

fakes = [
    User("kwijobo","abc"),
    User(name="emerged", hash="xyz")
]

def find(name:str) ->User|None:
    for e in fakes:
        if e.name == name:
            return e
    return None

def check_missing(name:str):
    if not find(name):
        raise Missing(f"Missing user {name}")

def check_duplicate(name:str):
    if find(name):
        raise Duplicate(f"Duplicate user {name}")
    
def get_all() -> list[User]:
    return fakes

def get_one(name: str) ->User:
    check_missing(name)
    return find(name)

def create(user:User)->User:
    check_duplicate(user)
    return user

def modify(name: str, user:User)->User:
    check_missing(name)
    return user

def delete(name: str) -> None:
    check_missing(name)
    return None 





