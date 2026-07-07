import logging
import os

# Create the logs folder if it doesn't already exist
os.makedirs("logs", exist_ok=True)

# Create a logger
logger = logging.getLogger("TradingBot")
logger.setLevel(logging.INFO)

# Avoid adding multiple handlers if imported more than once
if not logger.handlers:

    # Log file path
    file_handler = logging.FileHandler("logs/trading.log")

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)