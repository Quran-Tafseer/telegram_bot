import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ROOT_PATH=os.path.dirname(os.path.abspath(__file__))
BOT_TOKEN=os.getenv('QURAN_TAFSEER_BOT_TOKEN')
TEMPLATE_PATH=os.path.join(ROOT_PATH, 'templates')