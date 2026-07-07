import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading Symbol")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order Quantity")
    parser.add_argument("--price", help="Price (Required for LIMIT Orders)")

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "LIMIT":

            if args.price is None:
                raise ValueError("LIMIT order requires --price")

            price = validate_price(args.price)

            print(f"Price    : {price}")

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price,
            )

        else:

            response = place_market_order(
                symbol,
                side,
                quantity,
            )

        print("\n========== ORDER RESPONSE ==========")

        print("Order ID      :", response.get("orderId"))
        print("Status        :", response.get("status"))
        print("Executed Qty  :", response.get("executedQty"))
        print("Average Price :", response.get("avgPrice", "N/A"))

        print("\n✅ Order Placed Successfully")

    except Exception as e:

        print("\n❌ Order Failed")
        print(e)


if __name__ == "__main__":
    main()