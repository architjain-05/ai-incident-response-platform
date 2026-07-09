import sys
from datetime import datetime
from pathlib import Path
from typing import Final

services_dir = Path(__file__).resolve().parent
if str(services_dir) not in sys.path:
    sys.path.insert(0, str(services_dir))

from log_client import build_payload, post_log

LOG_TIMESTAMP_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"


def emit_log(service: str, level: str, message: str) -> None:
    timestamp = datetime.now().strftime(LOG_TIMESTAMP_FORMAT)
    payload = build_payload(timestamp=timestamp, service=service, level=level, message=message)
    post_log(payload)
