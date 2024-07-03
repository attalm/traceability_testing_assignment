"""
Tests for JsonHandler class in json_handler.py.
"""

import pytest
from json_handler import JsonHandler  # assuming the class is in json_handler.py

def requirement(requirement_id):
    """
    Decorator function to mark a test function with a requirement ID.
    """
    def decorator(function):
        function.requirement = requirement_id
        return function
    return decorator

@pytest.fixture
def json_handler():
    """
    Fixture to provide an instance of JsonHandler.
    """
    return JsonHandler()

@pytest.fixture
def temp_file(tmp_path):
    """
    Fixture to provide a temporary file path.
    """
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler, temp_file):
    """
    Test reading JSON data from a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler, temp_file):
    """
    Test writing and reading JSON data to/from a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler):
    """
    Test checking the existence of a key in JSON data.
    """
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(another_json_handler, another_updated_file):
    """
    Test updating JSON data in a file.
    """
    data = {"test": "data"}
    another_json_handler.write_json(data, another_updated_file)
    another_json_handler.update_json("test", "new data", another_updated_file)
    updated_data = another_json_handler.read_json(another_updated_file)
    assert updated_data["test"] == "new data"


