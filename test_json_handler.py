import pytest
from json_handler import JsonHandler


def requirement(id):
    def decorator(function):
        function.requirement = id
        return function
    return decorator


@pytest.fixture
def json_handler() -> JsonHandler:
    """Provides an instance of JsonHandler for tests."""
    return JsonHandler()


@pytest.fixture
def updated_file(tmp_path) -> str:
    """Provides a temporary JSON file path for tests."""
    return tmp_path / "test.json"


@requirement("REQ-101")
def test_read_json(json_handler: JsonHandler, updated_file: str) -> None:
    """Tests reading JSON data from a file."""
    data = {"test": "data"}
    json_handler.write_json(data, updated_file)
    read_data = json_handler.read_json(updated_file)
    assert read_data == data


@requirement("REQ-102")
def test_write_json(json_handler: JsonHandler, updated_file: str) -> None:
    """Tests writing JSON data to a file."""
    data = {"test": "data"}
    json_handler.write_json(data, updated_file)
    read_data = json_handler.read_json(updated_file)
    assert read_data == data


@requirement("REQ-103")
def test_check_key(json_handler: JsonHandler) -> None:
    """Tests checking if a key exists in a dictionary."""
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')


@requirement("REQ-104")
def test_update_json(json_handler: JsonHandler, updated_file: str) -> None:
    """Tests updating a JSON file with a new key-value pair."""
    data = {"test": "data"}
    json_handler.write_json(data, updated_file)
    json_handler.update_json("test", "new data", updated_file)
    updated_data = json_handler.read_json(updated_file)
    assert updated_data["test"] == "new data"
