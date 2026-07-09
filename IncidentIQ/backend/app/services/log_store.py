from typing import List

from ..schemas.log import LogEntry, LogLevel

logs: List[LogEntry] = []


def add_log(entry: LogEntry) -> None:
    logs.append(entry)


def get_all_logs() -> List[LogEntry]:
    return logs


def get_logs_by_service(service: str) -> List[LogEntry]:
    return [log for log in logs if log.service.lower() == service.lower()]


def get_logs_by_level(level: LogLevel) -> List[LogEntry]:
    return [log for log in logs if log.level == level]
