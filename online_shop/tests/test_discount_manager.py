from unittest.mock import Mock, call

from discounts import DiscountManager
from model_objects import DiscountData, Product, User


class SpyNotifier:
    def __init__(self):
        self.notified_users = []

    def notify(self, user, message):
        # don't send any messages from the unit test, record which users are notified
        self.notified_users.append(user)
        pass


def test_discount_for_users():
    notifier = SpyNotifier()
    discount_manager = DiscountManager(notifier)
    product = Product("headphones")
    product.discounts = []
    discount_details = DiscountData("10% off")
    users = [User("user1", [product]), User("user2", [product])]

    discount_manager.create_discount(product, discount_details, users)

    assert product.discounts == [discount_details]
    assert users[0] in notifier.notified_users
    assert users[1] in notifier.notified_users


def test_discount_for_users_with_mocking_framework():
    notifier = Mock()
    discount_manager = DiscountManager(notifier)
    product = Product("headphones")
    product.discounts = []
    discount_details = DiscountData("10% off")
    users = [User("user1", [product]), User("user2", [product])]

    discount_manager.create_discount(product, discount_details, users)

    assert product.discounts == [discount_details]
    expected_calls = [
        call(users[0], f"You may be interested in a discount on this product! {product.name}"),
        call(users[1], f"You may be interested in a discount on this product! {product.name}"),
    ]
    notifier.notify.assert_has_calls(expected_calls);
