import pytest

from animals.animals import sample_function
from animals.animals import Animals

@pytest.fixture
def Animals_object():
    return Animals()

def test_Animals_instance_has_sample_method(Animals_object):
    assert hasattr(Animals_object, "sample_method")



def test_animals_has_sample_function():
    assert sample_function() is None  # no return value
