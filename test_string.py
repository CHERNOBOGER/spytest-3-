# test_string_utils.py
import pytest
from string_operations import get_string_length

@pytest.fixture
def test_data():
    return [
        ("", 0),
        ("Hello\nWorld", 11),
        ("   ", 3)
    ]

def test_string_lengths(test_data):
    for s, expected_length in test_data:
        assert get_string_length(s) == expected_length
        print(f"Test string '{s}': PASSED")