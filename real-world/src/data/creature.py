from sqlite3 import IntegrityError
from model.creature import Creature
from .init import conn, curs
from errors import Duplicate, Missing


curs.execute("""
    create table if not exists creature(
             name text primary key,
             country text,
             area text,
             description text,
             aka text
    )
""")

def row_to_model(row:tuple)->Creature:
    name,country,area,description,aka = row # 
    print(row[0],row[1],row[2],row[3],row[4],"((((()))))",name,area,description,country,aka)
    return Creature(name=name, country=country,area=area,description=description,aka=aka)

def model_to_dict(creature:Creature) ->dict:
    return creature.model_dump()

def get_one(name:str) -> Creature:
    qry = "select name,country,area,description,aka from creature where name=:name"
    params={"name":name}
    curs.execute(qry, params)
    row = curs.fetchone()
    print(row,'=====')
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Explorer {name} not found")

def get_all()->list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]

def create(creature:Creature) -> Creature:
    qry ="""insert into creature values
    (:name,:country,:area,:description,:aka)
    """
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(f"Explorer {creature.name} already exists")

    return get_one(creature.name)

def modify(creature:Creature):
    qry = """
    update creature
    set 
    name = :name,
    country = :country,
    area = :area,
    description = :description,
    aka = :aka
    where name = :name_original 
    """
    params = model_to_dict(creature)
    params["name_original"] = creature.name
    print(params,"-=-=-")
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(f"Creature {creature.name} not found.")

def replace(creature:Creature):
    return creature

def delete(name:str) -> bool:
    qry = "delete from creature where name = :name"
    params =  {"name":name}
    _ = curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(f"Creature {name} not found")
    return True




