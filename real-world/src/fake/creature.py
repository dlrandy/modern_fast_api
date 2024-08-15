from model.creature import Creature

_creatures = [
    Creature(
       name="yeti",
    country="CN",
    area="Himalayas",
    description="himalayas",
    aka="snowman"
    ),
    Creature(
        name="Bigfoot",
        aka="yeti;s cousin",
        country="CN",
        area="Himalayas",
        description="Hirsute "
    ),
]

def get_All() -> list[Creature]:
    """return all creatures"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature:Creature) -> Creature:
    """Add a creature"""
    return creature

def modify(creature:Creature) -> Creature:
    """partially modify a creature"""
    return creature

def replace(creature:Creature) -> Creature:
    """Completely replace a creature"""
    return creature

def delete(name: str):
    """delete a creature;return None if it existed"""
    return None


