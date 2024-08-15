from model.creature import Creature

from service import creature as code

sample = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="himalayas",
    aka="snowman"
)


def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one("yeti")
    assert resp == sample

def test_get_missing():
    resp = code.get_one("SSSS")
    assert resp is None


