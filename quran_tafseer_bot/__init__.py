from settings import BOT_TOKEN, SENTRY_DSN
from telegram.ext import Updater, CommandHandler
import logging
from commands import (start,  book_list, set_book, tafseer)
import sentry_sdk

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.ERROR
)
# Enable Sentry logging
sentry_sdk.init(SENTRY_DSN)

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

# Map command with functions
start_handler = CommandHandler('start', start)
book_list_handler = CommandHandler('books', book_list)
set_book_handler = CommandHandler('setbook', set_book, pass_args=True)
tafseer_handler = CommandHandler('tafseer', tafseer, pass_args=True)


# Add the mapping
dispatcher.add_handler(start_handler)
dispatcher.add_handler(book_list_handler)
dispatcher.add_handler(set_book_handler)
dispatcher.add_handler(tafseer_handler)
