import logging

import sentry_sdk
from telegram.ext import CommandHandler, Updater

from quran_telegram_bot.commands import book_list, set_book, start, tafseer
from quran_telegram_bot.database import database
from quran_telegram_bot.settings import BOT_TOKEN, SENTRY_DSN

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
