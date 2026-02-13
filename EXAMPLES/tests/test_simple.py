import pytest
# tests should begin with "test" for automatic discovery
def test_two_plus_two_equals_four():  
    assert 2 + 2 == 4   # if assert statement succeeds, the test passes

def test_three_is_greater_than_two():
    print("wackiness!")
    assert 2 < 3

def test_silly():
    assert True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])