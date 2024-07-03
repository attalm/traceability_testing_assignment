"""
Tests for JsonHandler class in json_handler.py.
"""
import tempfile
import pytest
from json_handler import JsonHandler


@pytest.fixture
def json_handler() -> JsonHandler:
    """Provides an instance of JsonHandler for tests."""
    return JsonHandler()


@pytest.fixture
def updated_file(tmp_path) -> str:
    """Provides a temporary JSON file path for tests."""
    return tmp_path / "test.json"


@pytest.fixture
def another_file(tmp_path) -> str:
    """Provides another temporary JSON file path for tests."""
    return tmp_path / "another_file.json"

def requirement(requirement_id):
    """
    Decorator function to mark a test function with a requirement ID.
    """
    def decorator(function):
        function.requirement = requirement_id
        return function
    return decorator


@requirement("REQ-101")
def test_read_json(json_handler: JsonHandler, updated_file: str):
    """
    Test reading JSON data from a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, updated_file)
    read_data = json_handler.read_json(updated_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler: JsonHandler, updated_file: str):
    """
    Test writing and reading JSON data to/from a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, updated_file)
    read_data = json_handler.read_json(updated_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler: JsonHandler, updated_file: str):
    """
    Test checking the existence of a key in JSON data.
    """
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler: JsonHandler, updated_file: str):
    """
    Test updating JSON data in a file.
    """
    data = {"test": "data"}
    json_handler.write_json(data, updated_file)
    json_handler.update_json("test", "new data", updated_file)
    updated_data = json_handler.read_json(updated_file)
    assert updated_data["test"] == "new data"
