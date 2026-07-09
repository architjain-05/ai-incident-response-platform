import json
from pathlib import Path
from typing import Any

import requests
from requests.exceptions import RequestException

BACKEND_URL = "http://localhost:8000/logs"


def post_log(payload: dict[str, Any]) -> None:
    """Send a log payload to the IncidentIQ backend.

    The call is fire-and-forget: failures are logged locally and do not stop
    the service from continuing.
    """
    try:
        response = requests.post(BACKEND_URL, json=payload, timeout=2)
        response.raise_for_status()
    except RequestException as exc:
        print(f"WARNING: Could not send log to backend: {exc}")


def build_payload(timestamp: str, service: str, level: str, message: str) -> dict[str, str]:
    return {
        "timestamp": timestamp,
        "service": service,
        "level": level,
        "message": message,
    }
