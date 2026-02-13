import os
import pytest

from .silly import Silly
    
# @pytest.fixture
# def silly_object():
#     return Silly()  # fixture returns instance of Silly

def test_silly_triples_value(silly_object):  # pass fixture as test parameter
    # silly_object = Silly()  NOT NEEDED
    assert silly_object.triple(5) == 15

NORMALIZE_DATA = [
    ("    Spam   ", "spam"),
    ("Spam    ", "spam"),
    ("spam", "spam"),
    (" spam ", "spam"),
    ("SPAM", "spam"),
]

@pytest.mark.parametrize("input,expected", NORMALIZE_DATA)
def test_silly_normalizes_string(silly_object, input, expected):
    assert silly_object.normalize(input) == expected

def test_builtin_fixture(tmp_path):
    print(f"{tmp_path.name = }")
    assert True
