from sqlite3 import IntegrityError
from model.explorer import Explorer
from .init import conn, curs
from errors import Missing,Duplicate

curs.execute("""
    create table if not exists explorer(
             name text primary key,
             description text,
             country text
    )
""")

def row_to_model(row:tuple)->Explorer:
    return Explorer(name=row[0],country=row[1], description=row[2])

def model_to_dict(explorer:Explorer) ->dict:
    return explorer.model_dump() if explorer else None

def get_one(name:str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params={"name":name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Explorer {name} not found")

def get_all()->list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]

def create(explorer:Explorer) -> Explorer:
    qry ="""insert into explorer values
    (:name,:country,:description)
    """
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(f"Explorer {explorer.name} already exists")

    return get_one(explorer.name)

def modify(name: str,explorer:Explorer):
    if not (name and explorer):
        return None
    qry = """
    update Explorer
    set country = :country,
    name = :name,
    description = :description
    where name = :name_orignal 
    """
    params = model_to_dict(explorer)
    params["name_original"] = explorer.name
    _ = curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(f"Explorer {name} not found")

def replace(explorer:Explorer):
    return explorer

def delete(name: str, explorer:Explorer) -> bool:
    if not name: return False
    qry = "delete from Explorer where name = :name"
    params =  {"name":name}
    _ = curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(f"Explorer {name} not found")
    return True




