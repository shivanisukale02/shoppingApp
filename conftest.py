
import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("opened amazon app")
    print("user logged in")
    yield
    print("user logged out")
    print("closed amazon app")