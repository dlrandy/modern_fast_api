from datetime import timedelta,datetime,timezone
import os 
from jose import jwt 
from model.user import User

TOKEN_EXPIRES = 15 # minutes

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data

from passlib.context import CryptContext

SECRET_KEY = "keep-it-secet-keep-it-safe"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def verify_password(plain: str, hash: str) -> bool:
    print("str",plain, hash)
    return pwd_context.verify(plain, hash)

def get_hash(plain:str) -> str:
    return pwd_context.hash(plain)

def get_jwt_username(token:str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except jwt.JWTError:
        return None
    return username

def get_current_user(token:str) -> User|None:
    if not (username := get_jwt_username(token)):
        return None
    if (user := lookup_user(username)):
        return user
    return None

def lookup_user(username: str) -> User|None:
    if (user := data.get_one(username)):
        return user
    return None

def auth_user(name: str, plain:str) -> User|None:
    if not (user := lookup_user(name)):
        return None
    print("userrrrrrrrrrr",user)
    if not verify_password(plain, user.hash):
        return None
    return user

def create_access_token(data:dict, expires: timedelta|None = None):
    src = data.copy()
    now = datetime.now(timezone.utc)
    expires = expires or timedelta(minutes=TOKEN_EXPIRES)
    src.update({"exp":now + expires})
    encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_all() -> list[User]:
    return data.get_all()

def get_one(name) -> User:
    return data.get_one(name)

def create(user: User) -> User:
    user.hash = get_hash(user.hash)
    return data.create(user)

def modify(name: str, user: User) -> User:
    return data.modify(name, user)

def delete(name: str) -> None:
    return data.delete(name)











