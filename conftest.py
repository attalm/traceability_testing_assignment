import pytest
from json_handler import JsonHandler


@pytest.fixture
def json_handler_instance():
    """
    Fixture to provide an instance of JsonHandler.
    """
    return JsonHandler()


@pytest.fixture
def updated_file(tmp_path):
    """
    Fixture to provide a temporary file path.
    """
    return tmp_path / "test.json"


@pytest.fixture
def another_file(tmp_path):
    """
    Fixture to provide another temporary file path.
    """
    return tmp_path / "another_file.json"


def pytest_runtest_protocol(item, nextitem):
    if hasattr(item, 'function') and hasattr(item.function, 'requirement'):
        print(f"Running test {item.nodeid} with requirement {item.function.requirement}")
    return None  # continue with the default test protocol

def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        result = 'NOT RUN'
        if call.excinfo is not None:
            if call.excinfo.typename == 'pytest.skip':
                result = 'SKIP'
            elif call.excinfo.typename == 'pytest.xfail':
                result = 'XFAIL'
            else:
                result = 'FAIL'
        else:
            result = 'PASS'
        item.config.traceability_matrix[item.nodeid] = (item.function.requirement, result)

def pytest_sessionstart(session):
    session.config.traceability_matrix = {}

def pytest_sessionfinish(session, exitstatus):
    print("Traceability Matrix:")
    for test, (requirement, result) in session.config.traceability_matrix.items():
        print(f"{test}: {requirement}, {result}")

