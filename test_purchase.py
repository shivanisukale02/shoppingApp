import pytest
@pytest.fixture()
def setUp():
    print("setup started")


def test_AddItemToCart(setUp):
    print("Added Successfully")

def test_RemoveItemToCart(setUp):
    print("Removed Successfully")
