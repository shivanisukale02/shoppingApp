import pytest
@pytest.fixture()
def setUp():
    print("opened amazon app")
    print("user logged in")
    yield
    print("user logged out")
    print("closed amazon app")

def test_placeOrder(setUp):
    print("Placing order")

def test_makePayment(setUp):
    print("To do the payment")

def test_orderConfirmation(setUp):
    print("Order Confirmed")