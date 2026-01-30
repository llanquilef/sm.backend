from datetime import datetime, timezone

def getTimeToUTC() -> datetime:
    return datetime.now(timezone.utc) 