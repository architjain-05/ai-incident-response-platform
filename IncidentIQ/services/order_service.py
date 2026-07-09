"""
Order Service simulation.

Generates mock orders-related events at random intervals and logs them.
"""

import random
import time
from typing import Final

from logger import get_logger
from service_base import emit_log

# Obtain logger for the ORDER service
SERVICE_NAME = "ORDER"
logger = get_logger(SERVICE_NAME)

# Events constants
INFO_EVENTS: Final[list[str]] = [
    "Order Created",
    "Order Confirmed",
    "Refund Initiated",
]

WARNING_EVENTS: Final[list[str]] = [
    "Order Delayed",
    "Customer Address Verification Pending",
]

ERROR_EVENTS: Final[list[str]] = [
    "Payment Verification Failed",
    "Order Cancellation Failed",
]

# Combined list of all events with their severity level
ALL_EVENTS: Final[list[tuple[str, str]]] = (
    [("INFO", event) for event in INFO_EVENTS]
    + [("WARNING", event) for event in WARNING_EVENTS]
    + [("ERROR", event) for event in ERROR_EVENTS]
)


def log_event(level: str, message: str) -> None:
    if level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)

    emit_log(SERVICE_NAME, level, message)


def run_service() -> None:
    """
    Run the Order Service simulation indefinitely.

    Selects a random event and logs it with the appropriate severity level,
    then sleeps for a random interval between 2 and 5 seconds.
    """
    logger.info("Order Service simulation started.")
    emit_log(SERVICE_NAME, "INFO", "Order Service simulation started.")

    while True:
        try:
            # Randomly choose an event and its level
            level, message = random.choice(ALL_EVENTS)
            log_event(level, message)

            # Sleep for a random interval between 2 and 5 seconds
            sleep_time = random.randint(2, 5)
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            logger.info("Order Service simulation stopped by user.")
            emit_log(SERVICE_NAME, "INFO", "Order Service simulation stopped by user.")
            break


if __name__ == "__main__":
    run_service()
