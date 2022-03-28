import pytest
@pytest.fixture()
def setUp():
    print("opened amazon app")
    print("user logged in")
    yield
    print("user logged out")
    print("closed amazon app")


def test_AddItemToCart(setUp):
    print("Added Successfully")

def test_RemoveItemToCart(setUp):
    print("Removed Successfully")
