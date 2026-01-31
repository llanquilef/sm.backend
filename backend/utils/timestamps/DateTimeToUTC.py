from datetime import datetime, timezone

def get_time_to_utc() -> datetime:
    return datetime.now(timezone.utc) 