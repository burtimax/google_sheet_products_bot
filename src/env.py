import os

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GOOGLE_CREDS_JSON_PATH = os.getenv('GOOGLE_CREDS_JSON_PATH')
GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID')
HF_TOKEN = os.getenv('HF_TOKEN')
HF_LLM_MODEL = os.getenv('HF_LLM_MODEL')
OPEN_AI_TOKEN = os.getenv('OPEN_AI_TOKEN')
OPEN_AI_MODEL = os.getenv('OPEN_AI_MODEL')