"""
General helper utilities — timestamps, formatters, validators.
"""

from __future__ import annotations

from datetime import datetime


def timestamp_now() -> str:
    """Return a human-readable timestamp for the current moment."""
    return datetime.now().strftime("%I:%M %p")


def format_date(dt: datetime | None = None) -> str:
    """Return a short date string, e.g. 'Apr 09'."""
    dt = dt or datetime.now()
    return dt.strftime("%b %d")


def clamp(value: int | float, lo: int | float, hi: int | float) -> int | float:
    """Clamp *value* between *lo* and *hi* inclusive."""
    return max(lo, min(hi, value))


def truncate(text: str, max_len: int = 120) -> str:
    """Truncate text to *max_len* characters, adding '…' if trimmed."""
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"
