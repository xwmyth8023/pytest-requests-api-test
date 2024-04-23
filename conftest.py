import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="append",
        default="qa",
        help="Choose your testing environment",
    )

@pytest.fixture(autouse=True, scope="function")
def get_env(request):
    print(request.config.getoption("--env"))

