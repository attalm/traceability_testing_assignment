import pytest
from json_handler import JsonHandler  # assuming the class is in json_handler.py

def requirement(id):
    def decorator(function):
        function.requirement = id
        return function
    return decorator

@pytest.fixture
def json_handler():
    return JsonHandler()

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler, temp_file):
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler, temp_file):
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler):
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')


@requirement("REQ-104")
def test_update_json(json_handler, temp_file):
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    json_handler.update_json("test", "new data", temp_file)
    updated_data = json_handler.read_json(temp_file)
    assert updated_data["test"] == "new data"
