import os

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GOOGLE_CREDS_JSON_PATH = os.getenv('GOOGLE_CREDS_JSON_PATH')
GOOGLE_SHEET_NAME = os.getenv('GOOGLE_SHEET_NAME')
HF_TOKEN = os.getenv('HF_TOKEN')