# test_json_handler.py

"""
Tests for JsonHandler class in json_handler.py.
"""




def requirement(requirement_id):
    """
    Decorator function to mark a test function with a requirement ID.
    """
    def decorator(function):
        function.requirement = requirement_id
        return function
    return decorator

@requirement("REQ-101")
def test_read_json(json_handler_instance, updated_file):
    """
    Test reading JSON data from a file.
    """
    data = {"test": "data"}
    json_handler_instance.write_json(data, updated_file)
    read_data = json_handler_instance.read_json(updated_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler_instance, updated_file):
    """
    Test writing and reading JSON data to/from a file.
    """
    data = {"test": "data"}
    json_handler_instance.write_json(data, updated_file)
    read_data = json_handler_instance.read_json(updated_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler_instance):
    """
    Test checking the existence of a key in JSON data.
    """
    data = {"test": "data"}
    assert json_handler_instance.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler_instance, another_file):
    """
    Test updating JSON data in a file.
    """
    data = {"test": "data"}
    json_handler_instance.write_json(data, another_file)
    json_handler_instance.update_json("test", "new data", another_file)
    updated_data = json_handler_instance.read_json(another_file)
    assert updated_data["test"] == "new data"
