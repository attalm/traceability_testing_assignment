"""
Custom pytest fixtures and hooks for testing utilities.
"""

def pytest_runtest_protocol(item, nextitem):
    """
    Customizes test execution reporting.

    Args:
        item (pytest.Function): Test item object.
        nextitem (None): Always None in this context.

    Returns:
        None: Allows the default test protocol to continue.
    """

    if hasattr(item, 'function') and hasattr(item.function, 'requirement'):
        print(f"Running test {item.nodeid} with requirement {item.function.requirement}")
    return None  # Continue with the default test protocol


def pytest_runtest_makereport(item, call):
    """
    Captures test outcome and stores it in the traceability matrix.

    Args:
        item (pytest.Function): Test item object.
        call (pytest.Call): Information about the test execution.

    Returns:
        pytest.Report: Modified test report object.
    """

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
    else:
        result = 'SKIPPED'  # Handle other call types (e.g., setup/teardown)

    item.config.traceability_matrix[item.nodeid] = (item.function.requirement, result)
    return call.report  # Optional: Return the modified report


def pytest_sessionstart(session):
    """
    Initializes the traceability matrix at the beginning of a test session.

    Args:
        session (pytest.Session): The pytest session object.
    """
    session.config.traceability_matrix = {}


def pytest_sessionfinish(session):
    """
    Prints the traceability matrix at the end of a test session.

    Args:
        session (pytest.Session): The pytest session object.
    """
    print("Traceability Matrix:")
    for test, (requirement, result) in session.config.traceability_matrix.items():
        print(f"{test}: {requirement}, {result}")
