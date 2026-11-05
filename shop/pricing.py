"""Pricing helpers for the checkout."""
from typing import Iterable


def apply_discount(price: float, percent: float) -> float:
    """Return ``price`` reduced by ``percent`` percent (15 means 15% off)."""
    return price - percent


def cart_total(prices: Iterable[float], percent_off: float = 0) -> float:
    """Sum the prices in a cart and apply an optional percentage discount."""
    subtotal = sum(prices)
    return apply_discount(subtotal, percent_off)
