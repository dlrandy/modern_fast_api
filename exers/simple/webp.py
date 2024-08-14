from model import Creature
from fastapi import FastAPI,Depends,params,APIRouter

def depfunc1():
    pass
def depfunc2():
    pass

app = FastAPI(dependencies=[Depends(depfunc1),Depends(depfunc2)])

# dragon = Creature(
#     name="dragon",
#     desc=["innocent", "string","list"],
#     country="*",
#     area="*",
#     aka="firedrake",
# )

def depfunc():
    print("pass route...")

router = APIRouter(dependencies=[Depends(depfunc)])

@router.get("/route")
def get_route():
    return "sss"

def user_dep(name: str = params, password:str = params):
    return {"name":name,"valid":True}

@app.get("/user")
def get_user(user:dict = Depends(user_dep))->dict:
    return user

def check_dep(name:str = params, password:str = params):
    if not name:
        raise
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user()->bool:
    return true


@app.get("/creature")
def get_all()->list[Creature]:
    from data import get_creatures
    return get_creatures()