from typing import List

from fastapi import APIRouter

from ..schemas.log import LogEntry, LogLevel
from ..services.log_store import add_log, get_all_logs, get_logs_by_level, get_logs_by_service

router = APIRouter(prefix="/logs", tags=["logs"])


@router.post("", response_model=dict)
async def create_log(entry: LogEntry) -> dict[str, str]:
    add_log(entry)
    return {"status": "success"}


@router.get("", response_model=List[LogEntry])
async def get_all_logs_endpoint() -> List[LogEntry]:
    return get_all_logs()


@router.get("/service/{service}", response_model=List[LogEntry])
async def get_logs_by_service_endpoint(service: str) -> List[LogEntry]:
    return get_logs_by_service(service)


@router.get("/level/{level}", response_model=List[LogEntry])
async def get_logs_by_level_endpoint(level: LogLevel) -> List[LogEntry]:
    return get_logs_by_level(level)
