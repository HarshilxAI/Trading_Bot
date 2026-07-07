import os

from dotenv import load_dotenv
from binance.um_futures import UMFutures

from bot.logging_config import logger

# Load variables from .env file
load_dotenv()


def get_client():
    """
    Creates and returns a Binance Futures Testnet client.
    """

    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("SECRET_KEY")

    if not api_key or not secret_key:
        raise ValueError(
            "API_KEY or SECRET_KEY is missing. Check your .env file."
        )

    logger.info("Creating Binance Futures Testnet client...")

    client = UMFutures(
        key=api_key,
        secret=secret_key,
        base_url="https://testnet.binancefuture.com"
    )

    logger.info("Client created successfully.")

    return client