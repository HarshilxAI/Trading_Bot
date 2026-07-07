"""
validators.py

This file contains helper functions to validate
user inputs before sending an order to Binance.
"""


def validate_symbol(symbol):
    """
    Checks whether the trading symbol is valid.
    Example: BTCUSDT, ETHUSDT
    """

    symbol = symbol.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT.")

    return symbol


def validate_side(side):
    """
    Checks whether the order side is valid.
    """

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type):
    """
    Checks whether the order type is valid.
    """

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity):
    """
    Quantity must be greater than zero.
    """

    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price):
    """
    Price must be greater than zero.
    """

    price = float(price)

    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    return price