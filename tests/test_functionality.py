from .example_package_michaelboerman.example import add_one

def test_add_one():
    assert add_one(1) == 2
    assert add_one(0) == 1
    assert add_one(-1) == 0
    assert add_one(-2) == -1


