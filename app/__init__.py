import os

from app import CustomWebEnginePage
from app import WebUI
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv('APP_NAME')
DEFAULT_HOST = os.getenv('APP_HOST')
DEFAULT_PORT = os.getenv('APP_PORT')


def IS_DEBUG():
    if os.getenv('ENV').lower() == 'production':
        return False
    return True


