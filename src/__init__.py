import os

from src import web
from src import gui
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv('APP_NAME')
DEFAULT_HOST = os.getenv('APP_HOST')
DEFAULT_PORT = os.getenv('APP_PORT')

MODEL_FILE = 'model.h5'
LABEL_FILE = "labels.txt"


def IS_DEBUG():
    if os.getenv('ENV').lower() == 'production':
        return False
    return True


