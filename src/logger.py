"""
TP3 — Structured JSON Logging
==============================
Create a reusable logger that outputs structured JSON logs.

Each log line should be a JSON object like:
    {"timestamp": "2026-03-18T10:30:00Z", "level": "INFO", "module": "extract", "function": "extract_products", "message": "..."}
"""

import json
import logging
from datetime import datetime, timezone


class JSONFormatter(logging.Formatter):
    """
    Custom log formatter that outputs JSON.

    Override the format() method to return a JSON string instead of plain text.
    """

    def format(self, record: logging.LogRecord) -> str:

        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "module": record.module,
            "function": record.funcName,
            "message": record.getMessage(),
        }

        if record.exc_info and record.exc_info[0] is not None:
            log_entry["exception"] = self.formatException(record.exc_info)

        # we add the ensure_ascii=False argument to allow for proper encoding of non-ASCII characters (like emojis) in the log messages
        return json.dumps(log_entry, ensure_ascii=False)


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a logger with JSON-formatted output.

    Args:
        name: Logger name (usually __name__ of the calling module)

    Returns:
        A configured logging.Logger instance
    """

    logger = logging.getLogger(name)
    # We only add a handler if none exist yet
    # This prevents duplicate log lines if get_logger() is called multiple times
    if not logger.handlers:
        # Create a StreamHandler() (outputs to console)
        handler = logging.StreamHandler()
        # Set its formatter to JSONFormatter()
        handler.setFormatter(JSONFormatter())
        # Add the handler to the logger
        logger.addHandler(handler)
        # Set the logger level to logging.DEBUG
        logger.setLevel(logging.DEBUG)

    return logger
