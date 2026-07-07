from binance.error import ClientError

from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    """
    Places a MARKET order on Binance Futures Testnet.
    """

    try:
        client = get_client()

        logger.info(
            f"Sending MARKET order | {side} | {symbol} | Qty={quantity}"
        )

        response = client.new_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        logger.info("Market order placed successfully.")

        return response

    except ClientError as e:
        logger.error(f"Binance API Error: {e}")

        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")

        raise


def place_limit_order(symbol, side, quantity, price):
    """
    Places a LIMIT order on Binance Futures Testnet.
    """

    try:
        client = get_client()

        logger.info(
            f"Sending LIMIT order | {side} | {symbol} | Qty={quantity} | Price={price}"
        )

        response = client.new_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        logger.info("Limit order placed successfully.")

        return response

    except ClientError as e:
        logger.error(f"Binance API Error: {e}")

        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")

        raise