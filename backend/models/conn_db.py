from sqlmodel import create_engine
import os

sqlite_db_name = os.environ.get('DB_NAME') 
sqlite_url = f'sqlite:///{sqlite_db_name}'

create_engine = create_engine(sqlite_url)
