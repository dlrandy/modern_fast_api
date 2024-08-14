from model import Creature
_creatures: list[Creature] = [
    Creature(
        name="yetr",
        country="CN",
        area="bejing",
        desc="hahahla",
        aka="aaasl"
    ),
    Creature(
        name="uussu",
        country="US",
        area="newyork",
        desc="hahass",
        aka="aaggl"
    ),
]

def get_creatures()->list[Creature]:
    return _creatures