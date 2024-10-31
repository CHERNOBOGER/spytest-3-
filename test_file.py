import os
import pytest
from string_operations import save_string_to_file

@pytest.fixture
def temp_file(tmpdir):
    file_path = tmpdir.join("test_file.txt")
    yield str(file_path)
    if os.path.exists(file_path):
        os.remove(file_path)

def test_save_string_to_file(temp_file):
    test_string = "Hello, World!"
    save_string_to_file(test_string, temp_file)
    
    with open(temp_file, 'r') as file:
        content = file.read()
    
    assert content == test_string
    print("Test save_string_to_file: PASSED")

def test_save_empty_string_to_file(temp_file):
    test_string = ""
    save_string_to_file(test_string, temp_file)
    
    with open(temp_file, 'r') as file:
        content = file.read()
    
    assert content == test_string
    print("Test save_empty_string_to_file: PASSED")