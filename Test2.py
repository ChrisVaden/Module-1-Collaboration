

import pytest
from calculator import square_number

def test_square_number_valid_input():
    """Test that a valid number returns the correct square."""
    assert square_number(5) == 25

def test_square_number_invalid_input():
    """Test that passing a non-number raises a TypeError."""
    with pytest.raises(TypeError):
        square_number("not_a_number")
    
    