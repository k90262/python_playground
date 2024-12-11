from discounts import DiscountManager
from model_objects import DiscountData, Product, User


class StubNotifier:
    def notify(self, user, message):
        # don't send any messages from the unit test
        pass


def test_discount_for_users():
    notifier = StubNotifier()
    discount_manager = DiscountManager(notifier)
    product = Product("headphones")
    product.discounts = []
    discount_details = DiscountData("10% off")
    users = [User("user1", [product]), User("user2", [product])]

    discount_manager.create_discount(product, discount_details, users)

    assert product.discounts == [discount_details]
