"""
Tests for JsonHandler class in json_handler.py.
"""

import pytest
from json_handler import JsonHandler  # assuming the class is in json_handler.py

@pytest.fixture
def json_handler_instance():
    """
    Fixture to provide an instance of JsonHandler.
    """
    return JsonHandler()

@pytest.fixture
def temp_file_path(tmp_path):
    """
    Fixture to provide a temporary file path.
    """
    return tmp_path / "test.json"

def requirement(id):
    """
    Decorator function to mark a test function with a requirement ID.
    """
    def decorator(function):
        function.requirement = id
        return function
    return decorator

@requirement("REQ-101")
def test_read_json(json_handler_instance, temp_file_path):
    """
    Test reading JSON data from a file.
    """
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_file_path)
    read_data = json_handler_instance.read_json(temp_file_path)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler_instance, temp_file_path):
    """
    Test writing and reading JSON data to/from a file.
    """
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_file_path)
    read_data = json_handler_instance.read_json(temp_file_path)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler_instance):
    """
    Test checking the existence of a key in JSON data.
    """
    data = {"test": "data"}
    assert json_handler_instance.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler_instance, temp_file_path):
    """
    Test updating JSON data in a file.
    """
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_file_path)
    json_handler_instance.update_json("test", "new data", temp_file_path)
    updated_data = json_handler_instance.read_json(temp_file_path)
    assert updated_data["test"] == "new data"
