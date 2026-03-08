import os
from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI()
ENV = load_dotenv(dotenv_path=os.environ.get('ENV'))
port = os.environ.get('PORT')
