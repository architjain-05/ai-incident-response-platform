from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, validator


class LogLevel(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class LogEntry(BaseModel):
    timestamp: str
    service: str
    level: LogLevel
    message: str

    @validator("timestamp")
    def validate_timestamp(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError as exc:
            raise ValueError("timestamp must be in YYYY-MM-DD HH:MM:SS format") from exc
        return value
