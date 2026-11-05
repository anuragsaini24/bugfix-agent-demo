from shop.pricing import apply_discount, cart_total


def test_cart_total_without_discount():
    assert cart_total([10, 20, 30]) == 60


def test_zero_percent_discount_changes_nothing():
    assert apply_discount(100, 0) == 100
