import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ROOT_PATH=os.path.dirname(os.path.abspath(__file__))
BOT_TOKEN=os.getenv('QURAN_TAFSEER_BOT_TOKEN')
TEMPLATE_PATH=os.path.join(ROOT_PATH, 'templates')
SENTRY_DSN=os.getenv('SENTRY_DSN', None)
