import heapq
from datetime import datetime
from pathlib import Path

LOG_FILES = [
    Path(__file__).resolve().parent.parent / "logs" / "order.log",
    Path(__file__).resolve().parent.parent / "logs" / "payment.log",
    Path(__file__).resolve().parent.parent / "logs" / "inventory.log",
    Path(__file__).resolve().parent.parent / "logs" / "database.log",
]

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_log_line(line: str, source: Path) -> tuple[datetime, str] | None:
    """Parse a single log line and return a tuple of timestamp and formatted output."""
    stripped = line.strip()
    if not stripped:
        return None

    try:
        timestamp_str = stripped[:19]
        timestamp = datetime.strptime(timestamp_str, TIMESTAMP_FORMAT)
        return timestamp, stripped
    except ValueError:
        print(f"WARNING: Skipping malformed log line in {source.name}: {line.strip()}")
        return None


def read_log_file(path: Path) -> list[tuple[datetime, str]]:
    """Read a log file and return parsed entries."""
    entries: list[tuple[datetime, str]] = []
    if not path.exists():
        print(f"WARNING: Log file not found: {path}")
        return entries

    try:
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                parsed = parse_log_line(line, path)
                if parsed is not None:
                    entries.append(parsed)
    except OSError as exc:
        print(f"WARNING: Could not read {path.name}: {exc}")

    return entries


def main() -> None:
    all_entries: list[tuple[datetime, str]] = []

    for path in LOG_FILES:
        all_entries.extend(read_log_file(path))

    all_entries.sort(key=lambda item: item[0])

    for _, text in all_entries:
        print(text)


if __name__ == "__main__":
    main()
