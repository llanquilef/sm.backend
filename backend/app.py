from fastapi import FastAPI
import os
from dotenv import load_dotenv

app = FastAPI()
env = load_dotenv(dotenv_path=os.environ.get('ENV'))
port = os.environ.get('PORT')
