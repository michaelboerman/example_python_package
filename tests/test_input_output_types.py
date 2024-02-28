import pytest
from src.example_package_michaelboerman.example import add_one

def test_expected_output_types():
    
    # expected inputs
    assert isinstance(add_one(5), int)
    assert isinstance(add_one(3.5), float)
    
def test_unexpected_input_types():
    
    # string input
    with pytest.raises(TypeError):
        add_one('abc')

    # boolean input
    with pytest.raises(TypeError):
        add_one(True)