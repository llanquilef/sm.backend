
from datetime import datetime
import datetime 

# Format UTC a String 
def format_UTC_to_string(created_at_timestamp: datetime):
    formattedData = datetime.datetime(created_at_timestamp).__repr__()
    #exactDayCreated = datetime.datetime(createdAtTimestamp).date()
    #year = datetime.datetime(createdAtTimestamp).year()
    return formattedData

