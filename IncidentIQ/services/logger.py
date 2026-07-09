"""
Logger module for the IncidentIQ simulation services.

Provides a reusable function `get_logger` to configure logging to both
a service-specific log file and the console/terminal.
"""

import logging
from pathlib import Path


def get_logger(service_name: str) -> logging.Logger:
    """
    Configure and return a logger for a specific microservice.

    Logs are written to 'logs/<service_name_lowercase>.log' and printed
    to the terminal in the format:
    YYYY-MM-DD HH:MM:SS | SERVICE | LEVEL | MESSAGE

    Args:
        service_name: The name of the service (e.g., 'ORDER', 'PAYMENT').

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(service_name)
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if the logger is already configured
    if not logger.handlers:
        # Resolve the 'logs' directory path relative to the services directory
        logs_dir = Path(__file__).resolve().parent.parent / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        # Build path to the log file (e.g. logs/order.log)
        log_file = logs_dir / f"{service_name.lower()}.log"

        # Log format: YYYY-MM-DD HH:MM:SS | SERVICE | LEVEL | MESSAGE
        log_format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

        # File Handler
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
